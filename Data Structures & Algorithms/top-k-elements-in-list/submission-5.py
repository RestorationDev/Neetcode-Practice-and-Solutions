class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        freq = [[] for i in range(len(nums) + 1)]

        output = []

        #create a frequency map for each value in nums
        for n in nums:
            count[n] = 1 + count.get(n,0)
        #then at the array idx, add our value, array idx signifies occurrance count
        for key, val in count.items():
            freq[val].append(key)

        #                start      stop  step
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output