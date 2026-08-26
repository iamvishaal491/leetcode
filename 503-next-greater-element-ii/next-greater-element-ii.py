class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            curr=nums[i]
            found=False
            for j in range(1,len(nums)):
                index=(i+j)%len(nums)
                if nums[index]>curr:
                    ans.append(nums[index])
                    found=True
                    break
            if found==False:
                ans.append(-1)
        return ans
        