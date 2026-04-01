class Solution:

    def encode(self, strs: List[str]) -> str:
        long_s = ""
        num_s = ""
        for s in strs:
            num_s += "#" + str(len(s))
            long_s += s  
        num_s += "#|"
        total_s = num_s + long_s

        return total_s

    def decode(self, s: str) -> List[str]:
        char_inc_arr = []
        fin_arr = []
        beg = 0
        i = 0
        curr_num = ""
        while s[i] != "|":
            i+=1
            if s[i] == "#":
                curr_num = s[beg+1:i]
                char_inc_arr.append(int(curr_num))
                beg = i
        beg += 2
        nexstr = s[beg:]
        beg = 0
        for n in char_inc_arr:
            fin_arr.append(nexstr[beg:beg+n])
            beg += n

        return fin_arr

            
            