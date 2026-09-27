class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = -1
        l = 0
        r = len(heights)-1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            if area > max_water:
                max_water = area
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_water