class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        high = arr.index(max(arr))
        if high == 0 or high == len(arr) - 1:
            return False
        for i in range (high):
            if arr[i]<arr[i+1]:
                continue
            else:
                return False
        for i in range(high, len(arr)-1):
            if arr[i] > arr[i + 1]:
                continue
            else:
                return False
        return True
            


        
        