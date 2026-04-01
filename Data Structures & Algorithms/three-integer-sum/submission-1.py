class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        trips = []

        for i in range(len(nums)):

            l, r = i + 1, len(nums) - 1

            if i > 0 and nums[i-1] == nums[i]:
                continue

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

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return trips

                
