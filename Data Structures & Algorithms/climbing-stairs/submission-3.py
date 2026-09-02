class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}        

        def dfs(stair):
            if stair == n:
                return 1
            if stair > n:
                return 0
            if stair in memo:
                return memo[stair]
            memo[stair] = dfs(stair + 1) + dfs(stair + 2) 
            return memo[stair]


        return dfs(0)