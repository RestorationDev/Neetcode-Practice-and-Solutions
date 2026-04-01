class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        res = set()

        for n in nums1:
            seen.add(n)

            #can just use set function but this works...
        for n in nums2:
            if n in seen:
                res.add(n)
            
        return list(res)
        