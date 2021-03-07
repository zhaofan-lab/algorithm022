class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        def DFS(cols, diag1, diag2, loc):
            if loc == n:
                self.count += 1
                return
            bit = (~(cols | diag1 | diag2)) & ((1 << n) - 1)
            while bit:
                p = bit & -bit
                bit &= (bit - 1)
                DFS(cols | p, (diag1 | p) << 1, (diag2 | p) >> 1, loc + 1)
        self.count = 0
        DFS(0, 0, 0, 0)
        return self.count