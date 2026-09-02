class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def bfs(flight):
            if flight >= len(cost):
                return 0

            newCost = cost[flight] + min(bfs(flight + 1 ), bfs(flight + 2))

            return newCost

        return min(bfs(0), bfs(1))