class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #first, we must obtain a prefix array, multiplying all previous values behind each num in arr
        #then, we do the same the other way around, postfix
        #can likely cover both in the same loop
        #lastly we multiply both these arrays together

        pre = [1] * len(nums)
        post = [1] * len(nums)
        fin = [1] * len(nums)

        j = len(nums) - 1

        for i in range(len(nums)):
            print(i,j)
            #continue if i == 0, otherwise multiply previous n in nums be resp p in post/pre
            if i == 0:
                j-=1
                continue
            

            pre[i] = nums[i-1] * pre[i-1]
            post[j] = nums[j+1] * post[j+1]

            j-=1
        
        for i in range(len(post)):
            fin[i] = post[i] * pre[i]

        return fin
        