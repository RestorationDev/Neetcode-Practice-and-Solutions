class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numhash = set()
        for value in nums:
            if value in numhash:
                return True
            else:
                numhash.add(value)

        return False

         