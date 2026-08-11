class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        ct = {}

        for r in range(len(s)):

            ct[s[r]] = ct.get(s[r],0) + 1

            #basically our way of looking in the window
            #and saying ok window len - most freq
            while r - l - max(ct.values()) + 1 > k:
                ct[s[l]] -= 1
                l += 1
            
            res = max(r-l + 1, res)
        return res
