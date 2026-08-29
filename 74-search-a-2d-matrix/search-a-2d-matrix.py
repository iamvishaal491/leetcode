class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        low=0
        high=(len(mat)*len(mat[0]))-1
        while(low<=high):
            mid=(low+high)//2
            row=mid//len(mat[0])
            col=mid%len(mat[0])
            if mat[row][col]==target:
                return True
            elif target>mat[row][col]:
                low=mid+1
            else:
                high=mid-1
        return False
        