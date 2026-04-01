class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        freq = [[] for i in range(len(nums) + 1)]

        output = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for key, val in count.items():
            freq[val].append(key)

        #loop bwds, handle null vals


        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output



