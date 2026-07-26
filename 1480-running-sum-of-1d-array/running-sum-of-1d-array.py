class Solution(object):
    def runningSum(self, nums):
        c=0
        stk=[]
        for i in range(0,len(nums)):
            c+=nums[i]
            stk.append(c)
        return stk        