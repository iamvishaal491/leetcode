class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans=0
        while n!=0: #34 / 5
            ans+=(n%k) #9
            n=n//k# 
        return ans