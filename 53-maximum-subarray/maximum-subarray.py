class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub=nums[0]
        cur=0
        for n in nums:
            if cur<0:
                cur=0
            cur+=n
            max_sub=max(max_sub,cur)
        return max_sub

        