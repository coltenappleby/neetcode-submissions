class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                subset.sort()
                if subset not in res:
                    res.append(subset.copy())
                return
            
            dfs(i+1)
            subset.append(nums[i])
            dfs(i+1)
            subset.remove(nums[i])
            return 
        dfs(0)
        return res