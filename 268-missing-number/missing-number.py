class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k=len(nums)
        tot=(k*(k+1))//2
        num_tot=sum(nums)
        return tot-num_tot
        
        
        