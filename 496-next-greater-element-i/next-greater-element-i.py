class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        for i in range(len(nums2)):
            curr=nums2[i]
            found=False
            for j in range(i+1,len(nums2)):
                if nums2[j]>curr:
                    d[curr]=nums2[j]
                    found=True
                    break
            if found==False:
                d[curr]=-1
        ans=[]
        for i in nums1:
            ans.append(d[i])
        return ans