class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot=sum(nums)
        if tot%2!=0:
            return False
        target=tot//2
        n=len(nums)
        dp=[0]*(target+1)
        dp[0]=1
        for num in nums:
            for j in range(target,num-1,-1):
                dp[j] =dp[j] or dp[j-num]
        return bool(dp[target])
        
        