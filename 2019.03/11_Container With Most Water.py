class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            b = right - left
            area = b * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            if max_area < area:
                max_area = area
        return max_area
