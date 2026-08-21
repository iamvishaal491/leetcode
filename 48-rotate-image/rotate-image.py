class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        for i in range(len(mat)):
            for j in range(i+1,len(mat)):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]  
        for i in mat:
            i=i.reverse()
        
        