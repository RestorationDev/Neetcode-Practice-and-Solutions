class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # first localize window to max non repeating substring
        # then expand the window from there

        start = 0
        dic = {}
        res = 0

        for end in range(len(s)):

            dic[s[end]] = dic.get(s[end], 0) + 1
            while end - start - max(dic.values()) + 1 > k:
                dic[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
        
        return res
            
            
                




        