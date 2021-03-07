class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        if n == 0:
            return []
        res = [intervals[0]]
        for i in range(1, n):
            if intervals[i][0] <= res[-1][1]:
                if intervals[i][1] > res[-1][1]:
                    res[-1][1] = intervals[i][1]
            else:
                res.append(intervals[i])
        return res