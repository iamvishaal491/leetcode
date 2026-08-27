class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev=0
        m=n
        while n>0:
            last=n%10
            rev=(rev*10)+last
            n=n//10
        return abs(rev-m)
        