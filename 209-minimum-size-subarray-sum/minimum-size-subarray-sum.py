class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len=float("inf")
        summ=0
        l=0
        for r in range(len(nums)):
            summ+=nums[r]
            while summ>=target:
                min_len=min(min_len,r-l+1)
                summ-=nums[l]
                l+=1
        return min_len if min_len<float("inf") else 0      