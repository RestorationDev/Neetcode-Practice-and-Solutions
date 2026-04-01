class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #enumerate through array
        #check if we have target - i
        #store some combination of index, val
        #need structure that optimally stores i, v pairs

        ts_d = {}
        for i, n in enumerate(nums):
            if target - n in ts_d.keys():
                return [ts_d[target-n], i]
            ts_d[n] = i
        print(ts_d)
        
        