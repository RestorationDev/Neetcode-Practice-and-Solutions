class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output_arr = []

        prefix = 1

        for num in nums:
            output_arr.append(prefix)
            prefix *= num
        
        postfix = 1
        i = 0
        for num in nums[::-1]:
            output_arr[len(nums)-i-1] *= postfix
            postfix *= num
            i += 1
        
        return output_arr       