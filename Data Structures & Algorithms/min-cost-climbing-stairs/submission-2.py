class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
        def dfs(flight):
            if flight > n:
                return math.inf
            if flight == n:
                return 0
            if flight in memo:
                return memo[flight]
            memo[flight] = cost[flight] + min(dfs(flight + 1), dfs(flight + 2))
            
            return memo[flight]
        
        return min(dfs(0), dfs(1))
        