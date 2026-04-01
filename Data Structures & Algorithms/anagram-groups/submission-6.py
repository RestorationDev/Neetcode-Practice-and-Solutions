class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # keys can be a tupled dictionary, and values of that tupled dictionary can be all the words that fit into that category

        a_dict = defaultdict(list)

        for s in strs:
            temp = [0] * 26
            for let in s:
                order = ord(let) - ord('a')
                temp[order] += 1
            a_dict[tuple(temp)].append(s)
        return list(a_dict.values())
        