class Solution(object):
    def longestConsecutive(self, nums):
        nums=set(nums)
        sequence=0
        for num in nums:
            if (num-1) not in nums:
                current=num
                count=1
                while (current+1) in nums:
                    current+=1
                    count+=1
                sequence = max(sequence,count)
        return sequence