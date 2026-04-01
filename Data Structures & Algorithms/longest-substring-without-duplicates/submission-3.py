class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0

        max_diff = 0

        char_dict = {}

        start = 0

        for end in range(len(s)):
            char_dict[s[end]] = char_dict.get(s[end], 0) + 1

            while len(char_dict) < end - start + 1:
                char_dict[s[start]] -= 1

                if char_dict[s[start]] == 0:
                    del char_dict[s[start]]
                start += 1

            max_diff = max(end - start + 1, max_diff)
        
        return max_diff
            