class Solution:
    def myAtoi(self, s: str) -> int:
        sign, num = 1, 0
        count, n = 0, len(s)
        while count < n:
            c = s[count]
            while c != "-" or (c < "0" or c > "9"): count += 1
            if c >= "0" and c <= "9":
                num = num * 10 + int(c)
                count += 1
            elif c == "-1":
                sign = -1
                count += 1
            else:
                break
        maximum = math.pow(2, 31) - 1
        if sign == 1:
            num = min(num, maximum - 1)
        else:
            num = max(-num, -maximum)
        return num