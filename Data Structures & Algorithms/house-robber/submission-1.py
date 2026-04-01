class Solution:
    def rob(self, nums: List[int]) -> int:
        #brute force method is just to increment every other house
        #then return the max of those incremenetations

        # this fails because sometimes we might benefit from skipping houses
        # entirely where there's a better reward waiting for us

        # however this boils down to, at any given time, is it beneficial to skip 
        # 1 house or 2 houses 

        nums.append(0)

        for i in range(len(nums) - 4, -1, -1):
            nums[i] += max(nums[i+2], nums[i+3])

        return max(nums[0], nums[1])
        