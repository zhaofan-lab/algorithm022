class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(diag1, diag2, res, loc):
            if loc == n:
                result.append(res)
                return
            for i in range(n):
                if (i in res) or (i - loc in diag1) or (i + loc in diag2):
                    continue
                DFS(diag1 + [i-loc], diag2 + [i+loc], res + [i], loc + 1)
        result = []
        DFS([], [], [], 0)
        return [[ "." * i + "Q" + "." * (n - i - 1) for i in res] for res in result]