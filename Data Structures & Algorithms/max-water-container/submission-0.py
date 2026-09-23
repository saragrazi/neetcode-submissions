class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxArea = min(heights[right], heights[left]) * (right -left)
        while left < right:
            if heights[left] <= heights[right]:
                left += 1
            else:
                right-=1
            maxArea = max(maxArea, (min(heights[right], heights[left]) * (right -left)))
                
        return maxArea