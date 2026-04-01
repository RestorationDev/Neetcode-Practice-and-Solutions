class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #we want a dictionary that captures a character frequency map as the key
        #we want same dictionary to capture the occurances of character frequency map
        #key is freq map, val is array of strings

        #create a temp dict, go through each strs, dict it, conv to tuple, find in strs or add
        #then append str to respective tuple area

        a_dict = defaultdict(list)
        freq_m = [0] * 26
        beg = ord("a")

        for s in strs:
            for l in s:
                pos = ord(l) - beg
                freq_m[pos] += 1
            a_dict[tuple(freq_m)].append(s)
            freq_m = [0] * 26
        
        return list(a_dict.values())
