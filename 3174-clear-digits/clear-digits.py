class Solution:
    def clearDigits(self, s: str) -> str:
        stk=[]
        for i in s:
            stk.append(i)
            if i.isdigit() and stk[-2].isalpha():
                stk.pop()
                stk.pop()
        return "".join(stk)
        