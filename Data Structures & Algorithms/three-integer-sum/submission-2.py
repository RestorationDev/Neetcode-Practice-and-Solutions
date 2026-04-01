class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #sort nums
        nums = sorted(nums)
        trips = []

        #loop through the array of nums
        for i in range(len(nums)):
            
            #initialize two pointers right next to position but not before...
            l, r = i + 1, len(nums) - 1

            #rule out duplicates by making sure there are no same values for leftmost ptr
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            #block (until else) controls 2 ptr logic -- adjusting right if too big, left if too small, both if right
            while l < r:
                tot = nums[i] + nums[l] + nums[r]

                if tot > 0:
                    r -= 1
                elif tot < 0:
                    l += 1
                else:
                    trips.append((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
                    
                    #this small block is important, it also controls duplicate logic on the left pointer
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return trips

                
