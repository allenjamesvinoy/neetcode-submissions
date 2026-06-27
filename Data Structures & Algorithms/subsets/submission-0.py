class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        subset = []
        nums_len = len(nums)

        def dfs(i):
            if i >= nums_len:
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res