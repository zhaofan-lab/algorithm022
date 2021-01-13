#贪心算法
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i, j = 0, 0

        g.sort()
        s.sort()
        len1 = len(g)
        len2 = len(s)
        while i < len1 and j < len2:
            if s[j] >= g[i]:
                i += 1
            j += 1

        return i