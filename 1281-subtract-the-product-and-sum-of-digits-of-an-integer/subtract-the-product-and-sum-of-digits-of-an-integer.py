class Solution(object):
    def subtractProductAndSum(self, n):
        k,m,o=0,1,0
        while (n>0):
            o=n%10
            k+=o
            m*=o
            n=n//10
        return m-k