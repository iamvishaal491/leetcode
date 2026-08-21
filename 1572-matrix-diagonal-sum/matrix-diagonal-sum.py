class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row,col,suma=0,0,0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if col==row:
                    suma+=mat[col][row]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if col!=row and col+row==len(mat)-1:
                    suma+=mat[col][row]
        return suma

        