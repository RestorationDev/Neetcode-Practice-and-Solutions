class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # width is measured by the index diff between the two bars
        # since this is a max problem, we initialze a max variable

        # height doesn't necessarily matter, if taller height and lesser width, can only trap the minimum amt of water
        # measuring heght of trappable water is min(l,r) * idx
        # let's start by moving in direction of the most water

        # BRUTE FORCE: Loop through every single bar pair, and return the maximum after iteration through every one

        l, r = 0, len(heights) - 1

        max_bucket = 0

        while l < r:

            area = min(heights[l], heights[r]) * (r-l)

            max_bucket = max(area, max_bucket)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_bucket
