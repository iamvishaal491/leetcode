class Solution:
    def coloredCells(self, n: int) -> int:
        m=0
        if n==1:
            return 1
        else:
            for i in range(1,n):
                m+=4*i
            m+=1
        return m
        