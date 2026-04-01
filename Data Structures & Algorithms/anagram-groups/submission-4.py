class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramDict = defaultdict(list)
        beginning = ord("a") 
        for s in strs:
            lis = [0] * 26
            for let in s:
                lis[ord(let) - beginning] += 1
            anagramDict[tuple(lis)].append(s)
        print(anagramDict.values())
        return list(anagramDict.values())
                