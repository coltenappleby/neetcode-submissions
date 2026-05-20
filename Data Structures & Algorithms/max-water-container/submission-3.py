class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        area = 0

        while L < R:
            w = R - L
            h = 0
            if heights[L] < heights[R]:
                h = heights[L]
                L += 1
            elif heights[L] > heights[R]:
                h = heights[R]
                R -= 1
            else:
                # heights are the same
                h = heights[R]
                R -= 1
                L += 1
            area = max(w * h, area)
        return area
            