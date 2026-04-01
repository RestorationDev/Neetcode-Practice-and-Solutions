class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        post = [1] * len(nums)
        pre = [1] * len(nums)
        fin = [1] * len(nums)

        i = 0
        j = len(nums) - 1
        for i in range(len(nums)):

            if i != 0:
                pre[i] = nums[i-1] * pre[i-1]

            if j != len(nums)-1:
                post[j] = nums[j+1] * post[j+1]

            i += 1
            j -= 1
        
        for i in range(len(nums)):
            fin[i] = post[i] * pre[i]

        print(post)
        print(pre)
        print(fin)
        return fin