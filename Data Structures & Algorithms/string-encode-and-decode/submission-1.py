class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:

        if not s:
            return []
        #we want to loop through string, read nums til delim
        #store nums in sizes, use ith position sizes to append that num, then onto next

        sizes, res, i = [], [], 0

        while i < len(s):
            cur = ""
            while s[i] != '#':
                cur += s[i]
                i += 1
            sizes.append(int(cur))

            res.append(s[i+1: i+1 + sizes[-1]]) 
            i += sizes[-1] + 1

        return res

            
        
   


#revisit














#SOL'N 1 -- UNDERSTOOD

# def encode(self, strs: List[str]) -> str:
        
#         #empty or none string
#         if not strs:
#             return ""
        
#         #initialize an array for the length of resp words, resulting encoded array
#         sizes, res = [], ""

#         #iter through strings and create a list of sizes
#         for s in strs:
#             sizes.append(len(s))
        
#         #iter through sizes and creates a comma sep str
#         # i.e. "9,2,3,4..."
#         for sz in sizes:
#             res += str(sz)
#             res += ','
#         res += '#'

#         #adds all resp strings
#         for s in strs:
#             res += s

#         return res

#      def decode(self, s: str) -> List[str]:
#         if not s:
#             return []
        
#         sizes, res, i = [], [], 0

#         #while loop handles going through entire number string
#         #inner while loop handles deliminators for words, adding to sizes arr
#         #the final i += 1 just moves past the hash symbol onto the following string words
#         while s[i] ! = '#':
#             cur = ""
#             while s[i] != ','
#                 cur += s[i]
#                 i+=1
#             sizes.append(int(cur))
#             i += 1
#         i += 1

#         # appends each string based on sizes given
#         for sz in sizes:
#             res.append(s[i:i + sz])
#             i += sz
#         return res





# WORKING SOLUTION: NOT USEFUL
 # def __init__(self):
    #     self.ed_dict = defaultdict(list)

    # def encode(self, strs: List[str]) -> str:

    #     self.ed_dict["word"] = tuple(strs)
    #     return "word"

    # def decode(self, s: str) -> List[str]:
    #     return list(self.ed_dict["word"])