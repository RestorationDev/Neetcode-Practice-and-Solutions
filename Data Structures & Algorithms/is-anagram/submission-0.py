class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_dict = {}
        anagram_dict_2 = {}

        for char in s:
            if char in anagram_dict:
                temp = anagram_dict[char]
                temp += 1
                anagram_dict.update({char : temp})
            else:
                anagram_dict.update({char: 1})
        
        for char in t:
            if char in anagram_dict_2:
                temp = anagram_dict_2[char]
                temp += 1
                anagram_dict_2.update({char : temp})
            else:
                anagram_dict_2.update({char: 1})
        
        return anagram_dict_2 == anagram_dict
        
        

        