class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_dict = defaultdict(int)
        k_array = k * [0]
        temp_index = 0

        for i in nums:
            nums_dict[i] += 1

        keys_list = list(nums_dict.keys())
        values_list = list(nums_dict.values())
        nums_list = list(nums_dict.items())

        k_array = sorted(nums_dict.items(),key=lambda item: item[1])

        k_array = k_array[::-1]

        print(nums_dict)
        print(values_list)
        print(keys_list)
        print(nums_list)
        print(k_array)

        final = []
        for tuple in k_array:
            final.append(tuple[0])
        print(final)

        return final[0:k]
        
        