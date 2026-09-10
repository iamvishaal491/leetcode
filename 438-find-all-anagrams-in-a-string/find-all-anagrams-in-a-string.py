class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d={}
        k=len(p)
        for i in range(k):
            if p[i] not in d:
                d[p[i]]=1
            else:
                d[p[i]]+=1
        left,right=0,0
        win={}
        stk=[]
        while right<len(s):
            if s[right] not in win:
                win[s[right]]=1
            else:
                win[s[right]]+=1
            right+=1
            if right-left>k:
                win[s[left]]-=1
                if win[s[left]]==0:
                    del win[s[left]]
                left+=1
            if right-left==k:
                if win==d:
                    stk.append(left)
        return stk
        