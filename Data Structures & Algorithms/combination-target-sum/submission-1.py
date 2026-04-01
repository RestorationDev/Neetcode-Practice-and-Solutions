class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(idx, path, total):

            if total == target:
                res.append(path.copy())
                return
            if idx >= len(nums) or total > target:
                return
            
            #with next list value in no skipping
            path.append(nums[idx])
            dfs(idx, path, total + nums[idx])
            #with skipping
            path.pop()
            dfs(idx + 1, path, total)
        
        dfs(0,[], 0)
        return res



