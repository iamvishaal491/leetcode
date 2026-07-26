class Solution(object):
    def shuffle(self, nums, n):
        left=0
        mid=len(nums)/2
        ans=[]
        for i in range(n):
            ans.append(nums[left])
            left+=1
            ans.append(nums[mid])
            mid+=1
        return ans 