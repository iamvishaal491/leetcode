class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        sign=0
        for i in nums:
            if i>0:
                sign^=0
            else:
                sign^=1
        return -1 if sign==1 else 1

        