class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(current, candidates):
            if len(current) == len(nums):
                res.append(current.copy())
                return

            for idx, candidate in enumerate(candidates):
                current.append(candidate)
                new_candidates = candidates.copy()
                new_candidates.pop(idx)
                dfs(current, new_candidates)
                current.pop()


        dfs([], nums)

        return res


