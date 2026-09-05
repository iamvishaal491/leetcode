class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            width = right - left
            if height[left] < height[right]:
                current_water = width * height[left]
                left += 1  
            else:
                current_water = width * height[right]
                right -= 1 
            if current_water > max_water:
                max_water = current_water   
        return max_water