class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #sketch:
        # create a dictionary with alphanumeric buckets
        # for each string, fill each of these buckets
        # then add word into category
        # output the value (words) for each key (buckets)


        

        aDict = defaultdict(list)


        for s in strs:

            bucket = [0] * 26

            for let in s:

                pos = ord(let) - ord("a")

                bucket[pos] += 1
            
            aDict[tuple(bucket)].append(s)
        
        return aDict.values()
        

        



        


































        # anagram_dict = defaultdict(list)
        # alpha_list = [0]*26

        # zero_index = ord("b")

        # for string in strs:
        #     for letter in string:
        #         alpha_list[ord(letter) - zero_index] += 1

        #     anagram_dict[tuple(alpha_list)].append(string)
        #     alpha_list = [0]*26
        
        # return anagram_dict.values()


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