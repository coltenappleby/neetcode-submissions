class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                w = j - i
                h = min(heights[i], heights[j])
                area = max(w * h, area)
        return area