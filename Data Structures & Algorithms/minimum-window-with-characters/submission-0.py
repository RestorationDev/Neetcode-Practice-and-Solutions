class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        tD = {}
        need = 0
        res = float("inf")
        resL = 0
        for char in t:
            tD[char] = tD.get(char, 0) + 1
            need += 1
        
        l = 0
        sD = {}
        have = 0
        for r in range(len(s)):
            if s[r] in tD:
                sD[s[r]] = sD.get(s[r], 0) + 1
                if sD[s[r]] == tD[s[r]]:
                    have += tD[s[r]]

            while need == have:
                if r - l + 1 < res:
                    res = r - l + 1
                    resL = l

                if s[l] in tD:
                    sD[s[l]] -= 1
                    if sD[s[l]] < tD[s[l]]:
                        have -= tD[s[l]]
                l += 1
        
        return "" if res == float("inf") else s[resL: resL + res]

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if not t or not s:
#             return ""

#         from collections import Counter

#         tD = Counter(t)
#         need = len(tD)          # number of distinct chars needed
#         have = 0

#         sD = {}
#         l = 0

#         resL = 0
#         resLen = float("inf")

#         for r in range(len(s)):
#             c = s[r]
#             if c in tD:
#                 sD[c] = sD.get(c, 0) + 1
#                 if sD[c] == tD[c]:
#                     have += 1

#             while have == need:
#                 # update best window
#                 if r - l + 1 < resLen:
#                     resLen = r - l + 1
#                     resL = l

#                 # shrink from left
#                 if s[l] in tD:
#                     sD[s[l]] -= 1
#                     if sD[s[l]] < tD[s[l]]:
#                         have -= 1
#                 l += 1

#         return "" if resLen == float("inf") else s[resL:resL + resLen]


