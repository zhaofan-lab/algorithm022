class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) > len(s):     
            return res
        dic = {}
        m = len(p)
        count = m
        for i in range(m):
            dic[p[i]] = dic.get(p[i], 0) +1   #记录所需元素及个数
        i = 0
        while i < len(s):
            if s[i] in dic:              
                dic[s[i]] -= 1               #如果S[i]在dic中存在，更新值
                if dic[s[i]] >= 0:           #如果dic[s[i]]<0,表明不需要这个数，不能更新count
                    count -= 1
            if i >= m:                       # 当i>=m, 弹出失效的字符，保证长度相等
                if s[i-m] in dic:
                    dic[s[i-m]] += 1        #s[i-m]未必一定在dic中，需要判断
                    if dic[s[i-m]] > 0:     #需要的数被弹出，更新count
                        count += 1
            if count == 0:
                res.append(i-m+1)
            i += 1
        return res