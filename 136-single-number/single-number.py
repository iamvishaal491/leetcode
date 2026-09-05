class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = 0
        for i in nums:
            m^=i
        return m
        