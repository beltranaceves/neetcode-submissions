class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        def dfs(house, robbed_first):
            if (house, robbed_first) in memo:
                return memo[(house, robbed_first)]
            if house >= len(nums):
                return 0
            if house == len(nums) - 1:
                return 0 if robbed_first else nums[house]

            memo[(house, robbed_first)] = max(dfs(house + 1, robbed_first), nums[house] + dfs(house + 2, robbed_first))

            return memo[(house, robbed_first)]

        return max(dfs(0, True), dfs(1, False))