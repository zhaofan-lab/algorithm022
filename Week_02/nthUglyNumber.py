class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp= [1]
        a, b, c = 0, 0, 0
        i = 1
        while i < n:
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp.append(min(n2, n3, n5))
            if dp[i] == n2: 
                a += 1
            if dp[i] == n3: 
                b += 1
            if dp[i] == n5: 
                c += 1
            i += 1
        return dp[-1]
