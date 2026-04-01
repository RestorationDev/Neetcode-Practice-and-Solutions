class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        res = 0
        ct = {}

        #res is the variable that holds the max str len upon replacements 
        # thus we want to track our maximum window even if the window shrinks
        # as such we need an update condition that cannot be overridden

        for r in range(len(s)):
            #look in current window
            #check if count - max char < k 
            #if not we shorten window
            ct[s[r]] = ct.get(s[r], 0) + 1

            while r - l - max(ct.values()) + 1 > k:
                ct[s[l]] -= 1
                l += 1

            res = max(r-l + 1, res)

        return res
            




            
                




        