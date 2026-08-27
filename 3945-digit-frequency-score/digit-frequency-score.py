class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        k={}
        ans=0
        while n>0:
            m=n%10
            if m not in k:
                k[m]=1
            else:
                k[m]+=1
            n=n//10
        for key,val in k.items():
            ans+=val*key
        return ans
        
        