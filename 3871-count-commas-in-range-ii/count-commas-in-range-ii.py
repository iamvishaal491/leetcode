class Solution:
    def countCommas(self, n: int) -> int:
        c=0
        k=1000
        while n>=k:
            c+=(n-k+1)
            k*=1000
        return c
        