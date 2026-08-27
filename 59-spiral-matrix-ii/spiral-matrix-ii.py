class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        ans=[]
        up,down,left,right=0,1,2,3
        i,j=0,0
        d=right

        up_wall=0
        right_wall=n
        down_wall=n
        left_wall=-1
        num=1

        while num<=n*n:
            if d==right:
                while j<right_wall:
                    mat[i][j]=num
                    num+=1
                    j+=1
                i,j=i+1,j-1
                right_wall-=1
                d=down
            elif d==down:
                while i<down_wall:
                    mat[i][j]=num
                    num+=1
                    i+=1
                i,j=i-1,j-1
                down_wall-=1
                d=left
            elif d==left:
                while j>left_wall:
                    mat[i][j]=num
                    num+=1
                    j-=1
                i,j=i-1,j+1
                left_wall+=1
                d=up
            else:
                if d==up:
                    while i>up_wall:
                        mat[i][j]=num
                        num+=1
                        i-=1
                    i,j=i+1,j+1
                    up_wall+=1
                    d=right
        return mat

        