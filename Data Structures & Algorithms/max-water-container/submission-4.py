class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr_max = 0

        i, j = 0, len(heights) - 1

        while i < j:
            if heights[i] >= heights[j]:
                curr_max = max(heights[j] * (j - i), curr_max)
                j -= 1
            elif heights[j] > heights[i]:
                curr_max = max(heights[i] * (j - i), curr_max)
                i += 1

        return curr_max
            
