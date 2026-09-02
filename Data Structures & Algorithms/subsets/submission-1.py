class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []
        def backtracking(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            backtracking(i + 1)
            subset.pop()
            backtracking(i + 1)

        backtracking(0)
        return res