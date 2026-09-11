class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            d[i]+=1
        for i in d.values():
            if i>2:
                return True
        return False
            
        