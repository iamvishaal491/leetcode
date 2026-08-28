class Solution:
    def countNegatives(self, mat: List[List[int]]) -> int:
        c=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]<0:
                    c+=1
        return c