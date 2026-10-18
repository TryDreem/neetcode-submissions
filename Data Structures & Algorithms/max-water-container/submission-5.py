class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mA = 0
        l, r = 0, len(heights) - 1
        while l < r:
            w = r - l
            mA = max(mA, w * min(heights[l], heights[r]))
            if heights[l] > heights[r]:
                r -= 1
            else: 
                l += 1
        return mA

            
