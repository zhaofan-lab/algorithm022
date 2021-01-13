class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills == None:
            return True
        if bills[0] == 10 or bills[0] == 20:
            return False
        d = {5:0, 10:0, 20:0}
        for i in bills:
            d[i] += 1
            if i != 5:
                if i == 10:
                    if d[5] > 0:
                        d[5] -= 1
                    else:
                        return False
                else:
                    if d[10] > 0 and d[5] > 0:
                        d[10] -= 1
                        d[5] -= 1
                    elif d[5] > 2:
                        d[5] -= 3
                    else:
                        return False
        return True