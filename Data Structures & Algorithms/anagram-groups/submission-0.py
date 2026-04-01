class Solution:
   
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = defaultdict(list)
        
        for str in strs:
            
            char_slots = [0] * 26

            for c in str:

                slot = ord(c) - ord("a")

                char_slots[slot] += 1
            
            anagram_dict[tuple(char_slots)].append(str)
        
        print(anagram_dict.values())
        return anagram_dict.values()



