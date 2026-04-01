class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {}

        for i, n in enumerate(nums):

            diff = target - n 

            if diff in prevNums:

                return [prevNums[diff], i] #return the index at the location of diff, and curr ind
            
            prevNums[n] = i # set the current key (the quantity) to index i
        
        #this works because it checks if the difference is in the dictionary
        #then it assigns the key associated with it if not
        #we are able to assign index after the loop because if it doesn't go through the loop
        #this means the difference doesn't exist which is why we store it for later
        #the map is a difference map meaning it's "b" in the eq'n a + b = c
        #we are given a in the form of every new n in nums, b has been stored previously
        #c is target