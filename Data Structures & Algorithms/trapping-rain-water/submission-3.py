class Solution:
    def trap(self, height: List[int]) -> int:
        

        # at each point we want to shift the minimum max pointer
        # and then subtract the minimum max ptr by the current height 
        # disregarding negative values


        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        area = 0
        #loop through numbers with 2 ptrs. 
        #we say that if the Max L/R pointer is smaller, we move in that direction and we subtract the Max L or Max R - height...
        #and we accumulate if that value is non-negative, otherwise we update mL or mR

        while l < r:

            
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                area += max_left - height[l]
                

            elif max_right < max_left:
                r -= 1
                max_right = max(max_right, height[r])
                area += max_right - height[r]
                

            else: 
                l += 1
                max_left = max(max_left, height[l])
                area += max_left - height[l]
                

        
        return area

                #in this case the maximum left height is chosen
                #and we subtract that maximum left height by the current left 
                #probably will also update accordingly, important to remember negative values are treated like 0



