class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        l=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        buck=[0]*(len(nums)+1)
        for i,j in d.items():
            if buck[j]==0:
                buck[j]=[i]
            else:
                buck[j].append(i)
        for i in range(len(nums),-1,-1):
            if buck[i]!=0:
                l.extend(buck[i])
            if len(l)==k:
                break
        return l

        
        