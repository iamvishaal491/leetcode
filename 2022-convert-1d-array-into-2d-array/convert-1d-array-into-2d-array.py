class Solution:
    def construct2DArray(self, ori: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(ori):
            return []
        mat=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                mat[i][j]=ori[i*n+j]
        return mat
            


        