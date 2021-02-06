class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        pre, cur = 1, 1
        for i in range(1, len(s)):
            temp = cur
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    cur = pre
                else:
                    return 0
            else:
                if s[i-1] == "1" or (s[i-1] == "2" and s[i] <= "6"):
                    cur = pre + temp

            pre = temp
        return cur