class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1, d2 = {}, {}
        res = []

        for n in nums1:
            d1[n] = d1.get(n, 0) + 1
        for n in nums2:
            d2[n] = d2.get(n, 0) + 1
        
        for key in d1:
            if key in d2:
                res.append(key)
        
        return res