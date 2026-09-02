class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums) - 1

        def dfs(house):
            if house == n:
                return nums[house]
            if house > n:
                return 0
            if house in memo:
                return memo[house]
            memo[house] = max(nums[house] + dfs(house + 2), dfs(house + 1))

            return memo[house]

        return dfs(0)