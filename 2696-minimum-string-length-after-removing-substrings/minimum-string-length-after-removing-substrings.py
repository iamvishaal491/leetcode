class Solution:
    def minLength(self, s: str) -> int:
        stk=[]
        for i in s:
            if stk and ((stk[-1]=="A" and i=="B") or (stk[-1]=="C" and i=="D")):
                stk.pop()
            else:
                stk.append(i)
        return len(stk)
        