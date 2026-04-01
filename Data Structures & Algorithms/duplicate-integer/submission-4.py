class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       numdict = defaultdict(int)

       for num in nums:
        numdict[num] += 1 
        if numdict[num] > 1:
            return True
       return False



































 # numhash = set()
        # for value in nums:
        #     if value in numhash:
        #         return True
        #     else:
        #         numhash.add(value)
        # return False