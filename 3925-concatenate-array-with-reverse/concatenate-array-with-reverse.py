class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        dup=nums[::-1]
        nums.extend(dup)
        return nums