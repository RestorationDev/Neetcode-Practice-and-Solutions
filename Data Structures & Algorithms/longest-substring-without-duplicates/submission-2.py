class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #as a referesher, sliding window technique works by
        #creating a window as conditions are met
        #shortening window (l->r) in this case

        if len(s) == 0:
            return 0

        char_dict = {}
        start = 0
        end = 1
        max_diff = 0

        for end in range(len(s)):

            char_dict[s[end]] = char_dict.get(s[end], 0) + 1

#want distinct elem per letter in window
#condition is while the len of dictionary is less than wdw size, bc we want it to be equal instead
            while len(char_dict) < end - start + 1:
                char_dict[s[start]] -= 1

                if char_dict[s[start]] == 0:
                    del char_dict[s[start]]
                start += 1
            max_diff = max(end - start + 1, max_diff)
            
        return max_diff
                


