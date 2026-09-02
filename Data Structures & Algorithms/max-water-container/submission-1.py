class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        if not heights or len(heights) == 1:
            return 0
        if len(heights) == 2:
            return 1 * min(heights[0], heights[1])

        l, r = 0, len(heights) - 1

        while l < r and r < len(heights):
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res