class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1:1}

        def bfs(height):
            if height in memo:
                return memo[height]
            
            memo[height] = bfs(height - 1) + bfs(height - 2)

            return memo[height]

        bfs(n)

        return memo[n]
