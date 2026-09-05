class Solution:
    def removeStars(self, s: str) -> str:
        stk=[]

        for i in s:
            if i=="*":
                stk.pop(-1)
            else:
                stk.append(i)

        return "".join(stk)
        