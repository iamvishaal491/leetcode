class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left=0
        c=0
        win=sum(arr[:k])
        if win//k >= threshold:
            c+=1
        for right in range (k, len(arr)):
            win-=arr[left]
            win+=arr[right]
            left+=1
            if win//k >= threshold:
                c+=1
        return c
        