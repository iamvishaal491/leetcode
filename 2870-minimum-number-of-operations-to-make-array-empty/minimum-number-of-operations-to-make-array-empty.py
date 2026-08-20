class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        c=0
        for i in d.values():
            if i==1:
                return -1
            else:
                c=c+(i+2)//3
        return c














       
        