class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def DFS(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            DFS(i+1, j)
            DFS(i-1, j)
            DFS(i, j+1)
            DFS(i, j-1)
        
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    DFS(i, j)
                    count += 1
        return count
        