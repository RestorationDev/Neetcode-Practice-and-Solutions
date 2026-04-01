class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            #3 possibilities: big, small, equal
            #for big: r - 1, for small l + 1, for equal, return positions

            tot = numbers[l] + numbers[r]

            if tot > target:
                r -= 1
            elif tot < target:
                l += 1
            else:
                return [l+1, r+1]


        