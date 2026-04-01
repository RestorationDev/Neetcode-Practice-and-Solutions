class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #remember our output is a key of alpha-list tuple
        #value of words corresponding to alpha-list tuple
        anagram_dict = defaultdict(list)
        alpha_list = [0]*26

        zero_index = ord("b")

        for string in strs:
            for letter in string:
                alpha_list[ord(letter) - zero_index] += 1

            anagram_dict[tuple(alpha_list)].append(string)
            alpha_list = [0]*26
        
        return anagram_dict.values()



































# class Solution:
   
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         anagram_dict = defaultdict(list)
        
#         for str in strs:
            
#             char_slots = [0] * 26

#             for c in str:

#                 slot = ord(c) - ord("a")

#                 char_slots[slot] += 1
            
#             anagram_dict[tuple(char_slots)].append(str)
        
#         print(anagram_dict.values())
#         return anagram_dict.values()