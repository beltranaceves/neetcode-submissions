class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def bfs(house):
            if house >= len(nums):
                return 0
            if house in memo:
                return memo[house]
            option_a = nums[house] + bfs(house + 2)
            option_b = bfs(house + 1)

            memo[house] = max(option_a, option_b)

            return memo[house]

        return bfs(0)