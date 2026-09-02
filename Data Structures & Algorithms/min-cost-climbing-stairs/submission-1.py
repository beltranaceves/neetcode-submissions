class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def bfs(flight):
            if flight >= len(cost):
                return 0

            if flight in memo:
                return memo[flight]
            newCost = cost[flight] + min(bfs(flight + 1 ), bfs(flight + 2))
            memo[flight] = newCost
            return newCost

        return min(bfs(0), bfs(1))