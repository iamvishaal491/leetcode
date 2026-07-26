class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set([numa for numa in nums1 for numb in nums2 if numa == numb]))    