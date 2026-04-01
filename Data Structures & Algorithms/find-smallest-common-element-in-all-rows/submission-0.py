class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        res = []
        for i in range(len(mat)-1):
            if i == 0:
                res = list(set(mat[i]) & set(mat[i + 1]))
                print(res)
                continue
            tmp = res
            res = list(set(tmp) & set(mat[i + 1]))

        return res[0]

