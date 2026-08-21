class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        stk=[]
        d={}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+j not in d:
                    d[i+j]=[mat[i][j]]
                else:
                    d[i+j].append(mat[i][j])
        for i,j in d.items():
            if i%2==0:
                stk.extend(j[::-1])   
            else:
                stk.extend(j)
        return stk

        