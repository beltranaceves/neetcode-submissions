class Solution:
    def clearIsland(self, idx, jdx, grid):
        if idx < 0 or idx >= len(grid) or jdx < 0 or jdx >= len(grid[0]):
            return

        if grid[idx][jdx] == "0":
            return

        if grid[idx][jdx] == "1":
            grid[idx][jdx] = "-1"
            self.clearIsland(idx + 1, jdx, grid)
            self.clearIsland(idx - 1, jdx, grid)
            self.clearIsland(idx, jdx + 1, grid)
            self.clearIsland(idx, jdx - 1, grid)
            return

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        for idx, row in enumerate(grid):
            for jdx, element in enumerate(row):
                if element == "1":
                    count += 1
                    self.clearIsland(idx, jdx, grid)
        return count
