class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums_set=set(nums)
        ans=[]
        for i in range(len(nums)):
            if i+1 not in nums_set:
                ans.append(i+1)
        return ans   