class Solution:
    def maxDepth(self, s: str) -> int:
        stk=[]
        ans=0
        for i in s:
            if i=="(":
                stk.append(i)
                ans=max(ans,len(stk))
            elif i==")":
                stk.pop()
        return ans
        
            
        