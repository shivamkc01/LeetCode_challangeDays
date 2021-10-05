#https://leetcode.com/problems/minimum-path-sum/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)   # 
        if m ==0:
            return 03
        n = len(grid[0])
        if n==0:
            # If there is no element we return 0
            return 0
        
        for i in range(0, m):   # for row
            for j in range(0, n):   # for column  
                # Checking if we can move either down or right
                if (i-1 >= 0 and j-1 >=0):
                    # we are taking a minimum value and add to current cell value
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                else:
                    # Here this is mean there is no path from down
                    if (i-1 >=0):
                        grid[i][j] += grid[i-1][j]
                        grid[i][j]
                    # This means there is only right down path 
                    if (j-1 >=0):
                        grid[i][j] += grid[i][j-1]                    
        # Returning bottom right value our answer
        return grid[l-1][n-1]
        