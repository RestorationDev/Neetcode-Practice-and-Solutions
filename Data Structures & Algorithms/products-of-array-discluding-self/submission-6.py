class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        fin = [1] * len(nums)

        j = len(nums) - 1

        for i in range(len(nums)):
            if i == 0:
                j -= 1
                continue
            pre[i] = nums[i - 1] * pre[i - 1]
            post[j] = nums[j + 1] * post[j + 1]

            j -= 1
        for i in range(len(post)):
            fin[i] = post[i] * pre[i]
        return fin

            

        