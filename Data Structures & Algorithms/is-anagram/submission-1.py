class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(list)
        t_dict = defaultdict(list)

        for l in s:
            if l in s_dict:
                s_dict[l] += 1
            else:
                s_dict[l] = 1
        
        for l in t:
            if l in t_dict:
                t_dict[l] += 1
            else:
                t_dict[l] = 1
        
        return s_dict == t_dict

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # anagram_dict = {}
        # anagram_dict_2 = {}

        # for char in s:
        #     if char in anagram_dict:
        #         temp = anagram_dict[char]
        #         temp += 1
        #         anagram_dict.update({char : temp})
        #     else:
        #         anagram_dict.update({char: 1})
        
        # for char in t:
        #     if char in anagram_dict_2:
        #         temp = anagram_dict_2[char]
        #         temp += 1
        #         anagram_dict_2.update({char : temp})
        #     else:
        #         anagram_dict_2.update({char: 1})
        
        # return anagram_dict_2 == anagram_dict
        
        

        