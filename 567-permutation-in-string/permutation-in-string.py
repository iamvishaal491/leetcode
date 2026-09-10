class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d={}
        k=len(s1)
        for i in range(k):
            if s1[i] not in d:
                d[s1[i]]=1
            else:
                d[s1[i]]+=1
        left,right=0,0
        win={}
        while right<len(s2):
            if s2[right] not in win:
                win[s2[right]]=1
            else:
                win[s2[right]]+=1
            right+=1
            if right-left>k:
                win[s2[left]]-=1
                if win[s2[left]]==0:
                    del win[s2[left]]
                left+=1
            if right-left==k:
                if win==d:
                    return True
        return False
        