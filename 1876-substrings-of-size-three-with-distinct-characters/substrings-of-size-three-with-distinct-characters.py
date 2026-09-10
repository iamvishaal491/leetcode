class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1
        left=0
        right=0
        win={}
        c=0
        while right<len(s):
            if s[right] not in win:
                win[s[right]]=1
            else:
                win[s[right]]+=1
            right+=1
            if right-left >3:
                win[s[left]]-=1
                if win[s[left]]==0:
                    del win[s[left]]
                left+=1
            if right-left==3:
                if len(win)==3:
                    c+=1
        return c



        