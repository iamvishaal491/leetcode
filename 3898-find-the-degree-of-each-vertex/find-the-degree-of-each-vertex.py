class Solution:
    def findDegrees(self, mat: list[list[int]]) -> list[int]:
        stk=[]
        for i in mat:
            stk.append(sum(i))
        return stk