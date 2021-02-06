class Solution:
    def union(self, p, i, j):
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        p[p1] = p2
    def parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            # 路径压缩
            x = i; i = p[i]; p[x] = root
        return root
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        count = 0
        p = [-1] * (m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    p[i * n + j] = i * n + j
                    count += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    for x,y in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                            if self.parent(p, i * n + j) != self.parent(p, x * n + y):
                                count -= 1
                            self.union(p, i * n + j, x * n + y)

        return count