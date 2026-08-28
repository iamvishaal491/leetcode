class Solution:
    def maxSum(self, mat: List[List[int]]) -> int:
        ans=0
        for i in range(len(mat)-2):
            for j in range(len(mat[0])-2):
                s = (mat[i][j] + mat[i][j+1] + mat[i][j+2] + mat[i+1][j+1] + mat[i+2][j] + mat[i+2][j+1] + mat[i+2][j+2])
                ans=max(ans,s)
        return ans

        