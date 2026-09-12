class Solution:
    def maxArea(self, heights: List[int]) -> int:
        _max = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            if (min(heights[l], heights[r]) * (r - l)) > _max:
                _max = min(heights[l], heights[r]) * (r - l)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return _max