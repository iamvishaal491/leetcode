class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        d={}
        l,res,win=0,0,0
        for r in range(len(nums)):
            if nums[r] not in d:
                d[nums[r]]=1
            else:
                d[nums[r]]+=1
            win+=1
            while len(d)>2:
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    del d[nums[l]]
                win-=1
                l+=1
            res=max(res,win)
        return res


        