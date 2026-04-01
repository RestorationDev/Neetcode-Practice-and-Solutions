class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #thought process to stimulate this is obv 3 ptrs
        #idea is to keep leftmost at one position and 
        

        # create 3 ptr variables
        # create an outer loop to go through variables L -> R

        res = []
        nums = sorted(nums)


        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l,r = i+1 , len(nums) - 1

            while l < r:

                tot = nums[i] + nums[l] + nums[r]

                if tot < 0:
                    l += 1
                elif tot > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    l, r = l+1, r-1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
