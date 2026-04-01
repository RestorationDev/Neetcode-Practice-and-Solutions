class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we know that we must use a difference, the question is where
        # we may subtract the target from the current num and if that diff exists, we add it to result
        # it takes n operations to check if something is in the array, would be better with a dict or set...

        dic = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dic.keys():
                return [dic[target-n], i]
            dic[n] = i
            


        