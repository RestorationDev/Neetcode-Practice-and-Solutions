class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for value in nums:
            count_of_value = nums.count(value)
            if count_of_value > 1:
                return True
    
        return False
         