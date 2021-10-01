class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid: List[List[str]], x, y):
            grid[x][y] = '0'
            if (x + 1 < len(grid) and grid[x + 1][y] == '1'):
                dfs(grid, x + 1, y)
            if (x - 1 >= 0 and grid[x - 1][y] == '1'):
                dfs(grid, x - 1, y)
            if (y - 1 >= 0 and grid[x][y - 1] == '1'):
                dfs(grid, x, y - 1)
            if (y + 1 < len(grid[0]) and grid[x][y + 1] == '1'):
                dfs(grid, x, y + 1)

        H, W = len(grid), len(grid[0])
        count = 0
        for i in range(0, H):
            for j in range(0, W):
                if (grid[i][j] == '1'):
                    count += 1
                    dfs(grid, i, j)
        return count

