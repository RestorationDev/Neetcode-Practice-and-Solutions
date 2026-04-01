class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        rightMax, leftMax = height[right], height[left]
        ctr = 0

        while left < right:
            
            #first we want to check if the right max or leftmax is smaller, take the smaller one
            #shift the smaller max and take the difference of it with the height, add it to ctr if >0

            if rightMax < leftMax:
                right -= 1
                if rightMax > height[right]:
                    ctr += rightMax - height[right]
                    print(ctr)
                rightMax = max(height[right], rightMax)
            
            elif rightMax >= leftMax:
                left += 1
                if leftMax > height[left]:
                    ctr += leftMax - height[left]
                    print(ctr)
                leftMax = max(height[left], leftMax)

            
        return ctr
            


            