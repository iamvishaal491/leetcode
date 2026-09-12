import os
import sys
import time
import json
import subprocess

try:
    from curl_cffi import requests
    USE_CURL_CFFI = True
except ImportError:
    import requests
    USE_CURL_CFFI = False

# ==================== CONFIGURATION ====================
CONFIG_FILE = "config.json"
CACHE_FILE = "export_progress.json"
GRAPHQL_URL = "https://leetcode.com/graphql"

# Extension mapping matching LeetSync Chrome Extension
LANG_EXTENSIONS = {
    "python": ".py",
    "python3": ".py",
    "cpp": ".cpp",
    "c++": ".cpp",
    "c": ".c",
    "java": ".java",
    "csharp": ".cs",
    "c#": ".cs",
    "javascript": ".js",
    "typescript": ".ts",
    "ruby": ".rb",
    "swift": ".swift",
    "go": ".go",
    "golang": ".go",
    "kotlin": ".kt",
    "scala": ".scala",
    "rust": ".rs",
    "php": ".php",
    "mysql": ".sql",
    "mssql": ".sql",
    "oraclesql": ".sql",
    "postgresql": ".sql",
    "sql": ".sql",
    "dart": ".dart",
    "elixir": ".ex",
    "racket": ".rkt",
    "erlang": ".erl"
}

DIFF_COLORS = {
    "Easy": "brightgreen",
    "Medium": "orange",
    "Hard": "red"
}

def load_config():
    """Loads configuration from config.json or environment variables."""
    config = {
        "LEETCODE_SESSION": os.environ.get("LEETCODE_SESSION", ""),
        "CSRF_TOKEN": os.environ.get("CSRF_TOKEN", ""),
        "COOKIE_HEADER": os.environ.get("COOKIE_HEADER", ""),
        "GITHUB_REPO_URL": os.environ.get("GITHUB_REPO_URL", ""),
        "OUTPUT_DIR": os.environ.get("OUTPUT_DIR", "."),
        "CREATE_GIT_COMMITS": True,
        "PRESERVE_SUBMISSION_DATES": True
    }
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                user_conf = json.load(f)
                config.update(user_conf)
        except Exception as e:
            print(f"[!] Warning: Could not parse {CONFIG_FILE}: {e}")
    return config

def get_session_and_headers(config):
    csrf = config.get("CSRF_TOKEN", "").strip()
    session_cookie = config.get("LEETCODE_SESSION", "").strip()
    full_cookie = config.get("COOKIE_HEADER", "").strip()
    uuuserid = config.get("UUUSERID", "").strip()
    random_uuid = config.get("RANDOM_UUID", "").strip()

    if full_cookie:
        cookie_val = full_cookie
    else:
        cookie_val = f"LEETCODE_SESSION={session_cookie}; csrftoken={csrf}"

    headers = {
        "authority": "leetcode.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "cookie": cookie_val,
        "origin": "https://leetcode.com",
        "referer": "https://leetcode.com/submissions/",
        "x-csrftoken": csrf
    }
    if uuuserid:
        headers["uuuserid"] = uuuserid
    if random_uuid:
        headers["random-uuid"] = random_uuid
    return headers

def post_graphql(payload, headers):
    kwargs = {
        "json": payload,
        "headers": headers,
        "timeout": 20
    }
    if USE_CURL_CFFI:
        kwargs["impersonate"] = "chrome124"
    return requests.post(GRAPHQL_URL, **kwargs)

def verify_session(headers):
    """Verifies if the provided session cookie is valid by testing submissionDetails."""
    # Test submissionDetails on known submission or userStatus
    query = """
    query userStatus {
        userStatus {
            isSignedIn
            username
        }
    }
    """
    try:
        r = post_graphql({"query": query}, headers)
        if r.status_code == 200:
            user_status = r.json().get("data", {}).get("userStatus", {})
            if user_status.get("isSignedIn"):
                return True, user_status.get("username", "")
    except Exception as e:
        print(f"[!] Verification request error: {e}")
    return False, ""

def fetch_all_accepted_submissions(headers):
    """
    Paginates through all submissions and extracts the latest accepted
    submission for every unique question.
    """
    query = """
    query subgroupSubmissionList($offset: Int!, $limit: Int!) {
        submissionList(offset: $offset, limit: $limit) {
            submissions {
                id
                title
                titleSlug
                statusDisplay
                lang
                timestamp
            }
            hasNext
        }
    }
    """
    offset = 0
    limit = 20
    has_next = True
    accepted_by_slug = {}
    total_scanned = 0

    print("[*] Fetching submission history from LeetCode...")
    while has_next:
        payload = {
            "query": query,
            "variables": {"offset": offset, "limit": limit}
        }
        resp = None
        for attempt in range(3):
            try:
                r = post_graphql(payload, headers)
                if r.status_code == 200:
                    resp = r.json().get("data", {}).get("submissionList", {})
                    break
                elif r.status_code == 429:
                    print("[!] Rate limited, sleeping 5 seconds...")
                    time.sleep(5)
            except Exception:
                time.sleep(2)

        if not resp:
            print(f"[!] Failed to fetch batch at offset {offset}. Stopping pagination.")
            break

        submissions = resp.get("submissions", []) or []
        has_next = resp.get("hasNext", False)
        total_scanned += len(submissions)

        for sub in submissions:
            if sub.get("statusDisplay") == "Accepted":
                slug = sub.get("titleSlug")
                if slug not in accepted_by_slug:
                    accepted_by_slug[slug] = sub

        print(f"    Scanned {total_scanned} submissions... Found {len(accepted_by_slug)} unique solved questions so far.")
        offset += limit
        time.sleep(0.5)

    return accepted_by_slug

def fetch_submission_details(submission_id, headers):
    """Fetches accepted code and performance stats for a specific submission."""
    query = """
    query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) {
            code
            timestamp
            statusCode
            runtime
            runtimeDisplay
            runtimePercentile
            memory
            memoryDisplay
            memoryPercentile
            lang {
                name
                verboseName
            }
            notes
        }
    }
    """
    payload = {
        "query": query,
        "variables": {"submissionId": int(submission_id)}
    }
    for attempt in range(3):
        try:
            r = post_graphql(payload, headers)
            if r.status_code == 200:
                data = r.json().get("data", {}).get("submissionDetails", {})
                if data:
                    return data
            elif r.status_code == 429:
                time.sleep(5)
        except Exception:
            time.sleep(2)
    return None

def fetch_question_data(title_slug, headers):
    """Fetches question frontend ID, title, difficulty, and HTML statement."""
    query = """
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            title
            titleSlug
            content
            difficulty
        }
    }
    """
    payload = {
        "query": query,
        "variables": {"titleSlug": title_slug}
    }
    for attempt in range(3):
        try:
            r = post_graphql(payload, headers)
            if r.status_code == 200:
                return r.json().get("data", {}).get("question", {})
            elif r.status_code == 429:
                time.sleep(5)
        except Exception:
            time.sleep(2)
    return None

def format_readme_leetsync(question):
    """Formats the README.md content exactly as LeetSync does."""
    title = question.get("title", "")
    slug = question.get("titleSlug", "")
    diff = question.get("difficulty", "Easy")
    content = question.get("content", "") or ""
    badge_color = DIFF_COLORS.get(diff, "brightgreen")

    badge = f"<img src='https://img.shields.io/badge/Difficulty-{diff}-{badge_color}' alt='Difficulty: {diff}' />"
    readme = f'<h2><a href="https://leetcode.com/problems/{slug}">{title}</a></h2> {badge}<hr>{content}'
    return readme

def format_notes_leetsync(title, notes):
    """Formats Notes.md content if notes exist."""
    return f"<h2>{title} Notes</h2><hr>{notes}"

def get_file_extension(lang_obj, fallback_lang):
    """Resolves file extension matching LeetSync logic."""
    if lang_obj and isinstance(lang_obj, dict):
        verbose = lang_obj.get("verboseName", "")
        name = lang_obj.get("name", "")
        for key in (verbose, name, verbose.lower(), name.lower()):
            if key in LANG_EXTENSIONS:
                return LANG_EXTENSIONS[key]
    if fallback_lang:
        for key in (fallback_lang, fallback_lang.lower()):
            if key in LANG_EXTENSIONS:
                return LANG_EXTENSIONS[key]
    return ".txt"

def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"exported_slugs": []}

def save_cache(cache):
    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, indent=2)
    except Exception as e:
        print(f"[!] Warning: Could not save cache: {e}")

def git_commit_problem(folder_path, commit_msg, timestamp, author_name, author_email):
    """Creates a git commit for the problem folder with original timestamp."""
    try:
        subprocess.run(["git", "add", folder_path], check=True, capture_output=True, text=True)
        date_str = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime(int(timestamp)))
        env = os.environ.copy()
        env["GIT_AUTHOR_NAME"] = author_name
        env["GIT_AUTHOR_EMAIL"] = author_email
        env["GIT_COMMITTER_NAME"] = author_name
        env["GIT_COMMITTER_EMAIL"] = author_email
        env["GIT_AUTHOR_DATE"] = f"{date_str} +0000"
        env["GIT_COMMITTER_DATE"] = f"{date_str} +0000"

        subprocess.run(["git", "commit", "-m", commit_msg], env=env, check=True, capture_output=True, text=True)
    except Exception as e:
        print(f"[!] Git commit error for {folder_path}: {e}")

def main():
    print("=" * 65)
    print("   LeetCode to GitHub Exporter (LeetSync Extension Format)")
    print("=" * 65)

    config = load_config()
    headers = get_session_and_headers(config)

    print("\n[*] Validating LeetCode session...")
    is_valid, username = verify_session(headers)
    if not is_valid:
        print("\n[X] Error: Session cookie is invalid or has expired.")
        print("    Please ensure you have refreshed leetcode.com and copied the fresh session cookie.")
        return 1

    print(f"[+] Authenticated successfully as LeetCode user: {username}")

    accepted_map = fetch_all_accepted_submissions(headers)
    print(f"\n[+] Total unique solved questions found: {len(accepted_map)}")

    if not accepted_map:
        print("[!] No accepted submissions found. Exiting.")
        return 0

    sorted_slugs = sorted(accepted_map.keys(), key=lambda s: accepted_map[s].get("timestamp", 0))

    cache = load_cache()
    exported_slugs = set(cache.get("exported_slugs", []))
    output_dir = config.get("OUTPUT_DIR", ".")
    create_commits = config.get("CREATE_GIT_COMMITS", True)
    github_repo = config.get("GITHUB_REPO_URL", "").strip()

    if create_commits and not os.path.exists(os.path.join(output_dir, ".git")):
        print("[*] Initializing local git repository...")
        subprocess.run(["git", "init"], cwd=output_dir, check=True)
        if github_repo:
            subprocess.run(["git", "remote", "add", "origin", github_repo], cwd=output_dir)

    author_name = "iamvishaal491"
    author_email = "vishaalramesh491@gmail.com"

    total = len(sorted_slugs)
    current = 0

    print(f"\n[*] Starting export of {total} questions in LeetSync format...\n")

    for slug in sorted_slugs:
        current += 1
        sub_meta = accepted_map[slug]
        sub_id = sub_meta.get("id")
        sub_title = sub_meta.get("title")
        sub_lang = sub_meta.get("lang")
        sub_time = sub_meta.get("timestamp", int(time.time()))

        if slug in exported_slugs:
            print(f"[{current}/{total}] (Skipped - already exported) {sub_title}")
            continue

        print(f"[{current}/{total}] Exporting: {sub_title} (Submission #{sub_id})...")

        details = fetch_submission_details(sub_id, headers)
        if not details or not details.get("code"):
            print(f"    [!] Warning: Could not retrieve code for {sub_title}. Skipping.")
            continue

        qdata = fetch_question_data(slug, headers)
        if not qdata:
            print(f"    [!] Warning: Could not retrieve problem statement for {slug}. Skipping.")
            continue

        frontend_id = qdata.get("questionFrontendId") or qdata.get("questionId") or "unknown"
        folder_name = f"{frontend_id}-{slug}"
        problem_dir = os.path.join(output_dir, folder_name)
        os.makedirs(problem_dir, exist_ok=True)

        readme_content = format_readme_leetsync(qdata)
        readme_path = os.path.join(problem_dir, "README.md")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(readme_content)

        ext = get_file_extension(details.get("lang"), sub_lang)
        sol_filename = f"{slug}{ext}"
        sol_path = os.path.join(problem_dir, sol_filename)
        with open(sol_path, "w", encoding="utf-8") as f:
            f.write(details.get("code", ""))

        notes = details.get("notes")
        if notes and notes.strip():
            notes_content = format_notes_leetsync(qdata.get("title", ""), notes)
            notes_path = os.path.join(problem_dir, "Notes.md")
            with open(notes_path, "w", encoding="utf-8") as f:
                f.write(notes_content)

        if create_commits:
            runtime_disp = details.get("runtimeDisplay") or f"{details.get('runtime', 0)} ms"
            runtime_pct = details.get("runtimePercentile") or 0.0
            mem_disp = details.get("memoryDisplay") or f"{details.get('memory', 0)} bytes"
            mem_pct = details.get("memoryPercentile") or 0.0

            commit_msg = f"Time: {runtime_disp} ({runtime_pct:.2f}%) | Memory: {mem_disp} ({mem_pct:.2f}%) - LeetSync"
            git_commit_problem(folder_name, commit_msg, sub_time, author_name, author_email)

        exported_slugs.add(slug)
        cache["exported_slugs"] = list(exported_slugs)
        save_cache(cache)

        time.sleep(0.4)

    print("\n" + "=" * 65)
    print(f" [+] Export complete! Successfully processed {len(exported_slugs)} questions.")
    print("=" * 65)

    if create_commits and github_repo:
        print("\n[*] Pushing to GitHub repository...")
        try:
            subprocess.run(["git", "branch", "-M", "main"], cwd=output_dir, check=True)
            subprocess.run(["git", "push", "-u", "origin", "main"], cwd=output_dir, check=True)
            print("[+] Successfully pushed to GitHub!")
        except Exception as e:
            print(f"[!] Push error: {e}")
            print("    You can push manually at any time by running:")
            print("    git push -u origin main")

    return 0

if __name__ == "__main__":
    sys.exit(main())
