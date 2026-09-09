class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        right=len(nums)-1
        win=sum(nums[:k])
        ans=win
        for right in range(k,len(nums)):
            win-=nums[left]
            win+=nums[right]
            left+=1
            ans=max(ans,win)
        return float(ans)/k
        