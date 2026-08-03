class Solution(object):
    def plusOne(self, digits):
        stk=[]
        result = int("".join(map(str, digits)))
        result+=1
        k=str(result)
        for i in k:
            stk.append(int(i))
        return stk 