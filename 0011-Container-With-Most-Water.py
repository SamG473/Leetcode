class Solution:
    def maxArea(self, height: list[int]) -> int:
        most = 0
        left = 0 
        right = len(height) - 1 

        while left < right:
            water = abs(left - right)
            area = water * min(height[left], height[right])
            
            if area > most:
                most = area
                
            if height[left] > height[right]:
                right -= 1 
            else:
                left += 1 


        return most 
