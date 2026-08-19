class Solution:
    def reverse(self,x):
        sign = -1 if x<0 else 1
        x=abs(x)
        r=0
        while x:
            digit=x%10
            r=r*10+digit
            x//=10
        r*=sign
        if r<-(2**31) or r>2**31:
            return 0
        return r