class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        premax=[0]*len(nums)
        premax[0]=nums[0]
        for i in range(len(nums)):
            premax[i]=max(premax[i-1],nums[i])

        suffmax=[0]*len(nums)
        suffmax[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            suffmax[i]=min(suffmax[i+1],nums[i])

        for i in range(len(nums)):
            if premax[i]-suffmax[i]<=k:
                return i
        return -1
        