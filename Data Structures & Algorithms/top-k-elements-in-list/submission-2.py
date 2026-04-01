class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #implementation attempt of bucket sort
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        
        for n,c in count.items():
            freq[c].append(n)

            
        

        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


            

                



































# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         nums_dict = defaultdict(int)
#         k_array = k * [0]
#         temp_index = 0

#         for i in nums:
#             nums_dict[i] += 1

#         keys_list = list(nums_dict.keys())
#         values_list = list(nums_dict.values())
#         nums_list = list(nums_dict.items())

#         k_array = sorted(nums_dict.items(),key=lambda item: item[1])

#         k_array = k_array[::-1]

#         print(nums_dict)
#         print(values_list)
#         print(keys_list)
#         print(nums_list)
#         print(k_array)

#         final = []
#         for tuple in k_array:
#             final.append(tuple[0])
#         print(final)

#         return final[0:k]
        
        