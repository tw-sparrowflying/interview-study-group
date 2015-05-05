class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        num = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == "1":
                    num = num + 1
                    grid = self.dfs(grid, i, j)
        return num
        
    def dfs(self, grid, x, y):
        grid[x][y] = "0"
        if y < len(grid[0])-1:
            if grid[x][y+1] == '1':
                grid = self.dfs(grid, x, y+1)
        if y > 0:
            if grid[x][y-1] == '1':
                grid = self.dfs(grid, x, y-1)
        if x > 0:
            if grid[x-1][y] == '1':
                grid = self.dfs(grid, x-1, y)
        if x < len(grid)-1:
            if grid[x+1][y] == '1':
                grid = self.dfs(grid, x+1, y)
        return grid