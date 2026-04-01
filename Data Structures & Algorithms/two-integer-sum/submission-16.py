class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        
        prevNums = {}


        for i, n in enumerate(nums):

            diff = target - n

            if diff in prevNums:

                return [prevNums[diff], i]
            
            prevNums[n] = i






                
                














# class Solution:
#     def twoSum(self, nums: List[int], target:int) -> List[int]:
#         prevMap = {}

#         for i, n in enumerate(nums):
#             diff = target - n

#             if diff in prevMap:
#                 return[prevMap[diff],i]
                
#             prevMap[n] = i

# prevMap stores the number as well as the index as it iterates through the list

# a for loop that iterates through a list with both the index and item is started
# we calculate a difference and check if it's in the prevmap, and if so, we return each idx


