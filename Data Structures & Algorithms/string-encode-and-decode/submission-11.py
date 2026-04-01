class Solution:
    
    #essentially convert the strings into one string, 
    #must encode information on how many characters to read, where to end, separation...
    #can add information at the beginning of the string

    def encode(self, strs: List[str]) -> str:

        st = ""
        words = ""
        wd_num = len(strs) - 1
        s_l = 0
        for i,s in enumerate(strs):
            s_l = len(s)
            words += s
            st += str(s_l) + "#"
        
        return st + "!" + words 


    def decode(self, s: str) -> List[str]:
        
        i = 0
        n_read = []
        n_str = ""
        output = []
        if s is None:
            return []
        while s[i] != "!":
            while s[i] != "#":
                n_str += s[i]
                i += 1
            n_read.append(int(n_str))
            n_str = ""
            i += 1
        i+=1    
        
        print(n_read)

        for n in n_read:
            output.append(s[i:i+n])
            i += n
        return output





