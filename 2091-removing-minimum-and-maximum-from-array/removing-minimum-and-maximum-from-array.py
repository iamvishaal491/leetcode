class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        max_ind=nums.index(max(nums))
        min_ind=nums.index(min(nums))
        i,j=sorted([min_ind,max_ind])
        opt1=j+1
        opt2=n-i
        opt3=i+1+n-j
        return min(opt1,opt2,opt3)

        