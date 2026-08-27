class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        p=0
        for i in nums:
            p+=i
        if p%k==0:
            return 0
        else:
            return p%k
                
        