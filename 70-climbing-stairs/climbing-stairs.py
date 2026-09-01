class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3:
            return n
        dp=[0]*(n+1)
        dp[2]=2
        dp[1]=1
        for p in range(3,n+1):
            dp[p]=dp[p-1]+dp[p-2]
        return dp[n]
        