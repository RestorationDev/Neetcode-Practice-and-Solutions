class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        freq = [[] for i in range(len(nums) + 1)]

        output = []

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for ke, v in count.items():
            freq[v].append(ke)
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output
