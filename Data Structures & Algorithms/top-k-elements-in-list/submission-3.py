class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #dictionary with key as num and value as # of occ of num
        count = {}

        #frequency is index, array val is number 
        freq = [[] for i in range(len(nums) + 1)]

        output = []

        #isolates num in count and adds 1 for freq
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        #at the count position (value of count dict), append the key...
        for num, cnt in count.items():
            freq[cnt].append(num)


        ct = 0
        #stops at zero since we odn't care what's at the 0 position
        #goes in reverse
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output
            
        
        
        print(count, freq)