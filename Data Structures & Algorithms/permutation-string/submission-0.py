class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #initialize a fixed length sliding window
        #a-z dictionaries for both, check all matches on the initialization
        #track matches in matches variable
        #keep moving window, as this is done, check for matches in the new start and new end (decriment prev start, increment new start)
        #lastly return true when all 26 matches are found...

        if len(s1) > len(s2):
            return False
        
        matches = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        s1d = {char: 0 for char in alphabet}
        s2d = {char: 0 for char in alphabet}

        #init both dicts
        for i in range(len(s1)):
            s1d[s1[i]] = s1d.get(s1[i], 0) + 1
            s2d[s2[i]] = s2d.get(s2[i], 0) + 1

        # find correspondences
        for key in s1d:
            if s1d[key] == s2d[key]:
                matches += 1
        
        #start window from a jumpstart of len(s1), keep moving, decrimenting start, incrementing end until end of str
        l, r = 0, len(s1)

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            s2d[s2[r]] += 1

            if s1d[s2[r]] == s2d[s2[r]]:
                matches += 1
            elif s1d[s2[r]] + 1  == s2d[s2[r]]:
                matches -= 1
            
            s2d[s2[l]] -= 1
            if s1d[s2[l]] == s2d[s2[l]]:
                matches += 1
            elif s1d[s2[l]] - 1 == s2d[s2[l]]:
                matches -= 1
            l += 1
        return matches == 26








        