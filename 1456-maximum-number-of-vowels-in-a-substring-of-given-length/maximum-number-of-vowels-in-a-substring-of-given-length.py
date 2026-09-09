class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow={"a","e","i","o","u"}
        c=0
        for i in range(k):
            if s[i] in vow:
                c+=1
        ans=c
        for i in range(k,len(s)):
            if s[i-k] in vow:
                c-=1
            if s[i] in vow:
                c+=1
            ans=max(ans,c)
        return ans

