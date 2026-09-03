class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        small=float('inf')
        for num in nums:
            if num%2==1:
                small=min(small,num)
        if small==float('inf'):
            return True
        for num in nums:
            if num%2==0 and num<=small:
                return False
        return True