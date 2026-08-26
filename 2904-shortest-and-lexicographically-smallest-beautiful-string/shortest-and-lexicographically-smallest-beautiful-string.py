class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        b = list(s)
        left = 0
        right = 0
        c = 0
        ans = ""
        while right < len(b):
            if b[right] == "1":
                c += 1
            while c > k:
                if b[left] == "1":
                    c -= 1
                left += 1
            if c == k:
                while b[left] == "0":
                    left += 1
                cur = "".join(b[left:right+1])
                if ans == "" or len(cur) < len(ans):
                    ans = cur
                elif len(cur) == len(ans) and cur < ans:
                    ans = cur
            right += 1
        return ans