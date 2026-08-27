class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        m,n=len(mat),len(mat[0])
        ans=[]
        up,down,left,right=0,1,2,3
        i,j=0,0
        d=right

        up_wall=0
        right_wall=n
        down_wall=m
        left_wall=-1

        while len(ans)!=m*n:
            if d==right:
                while j<right_wall:
                    ans.append(mat[i][j])
                    j+=1
                i,j=i+1,j-1
                right_wall-=1
                d=down
            elif d==down:
                while i<down_wall:
                    ans.append(mat[i][j])
                    i+=1
                i,j=i-1,j-1
                down_wall-=1
                d=left
            elif d==left:
                while j>left_wall:
                    ans.append(mat[i][j])
                    j-=1
                i,j=i-1,j+1
                left_wall+=1
                d=up
            else:
                if d==up:
                    while i>up_wall:
                        ans.append(mat[i][j])
                        i-=1
                    i,j=i+1,j+1
                    up_wall+=1
                    d=right
        return ans
        