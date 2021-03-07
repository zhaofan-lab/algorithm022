class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(cols, diag1, diag2, res, loc):
            if loc == n:
                result.append(res)
                return
            bit = (~(cols | diag1 | diag2)) & ((1 << n) - 1)
            while bit:
                p = bit & -bit
                bit &= (bit - 1)
                count = 0
                while p != (1 << count):
                    count += 1
                DFS(cols | p, (diag1 | p) << 1, (diag2 | p) >> 1, res + [count], loc + 1)
        result = []
        DFS(0, 0, 0, [], 0)
        return [[ "." * i + "Q" + "." * (n - i - 1) for i in res] for res in result]