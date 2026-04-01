class Solution:

    def encode(self, strs: List[str]) -> str:
        #provide seperation indications, length indicators, stopping condition
        s = ""
        for st in strs:
            s += str(len(st))
            s += "#"
        s += '|'

        for st in strs:
            s += st
        return s

    def decode(self, s: str) -> List[str]:
        
        ind_ls = []
        output = []
        i = 0
        while s[i] != '|':
            temp = ""
            while s[i] != '#':
                temp += s[i]
                i += 1
            ind_ls.append(int(temp))
            i += 1
        i += 1
        for n in ind_ls:
            output.append(s[i: i + n])
            i += n

        return output

        
