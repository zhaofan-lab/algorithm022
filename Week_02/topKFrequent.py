#解法一 排序
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d  = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        l = list(d.values())
        l.sort(reverse=True)
        result = []
        for i in range(0, k):
            for key in d:
                if d[key] == l[i]:
                    result.append(key)
        a = list(set(result))
        return a

#解法二：堆
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.Counter(nums)
        result = []
        heap = []
        for num, freq in d.items() :
            # 如果堆满了（k个元素）
            if len(heap) == k :
                # 弹出最小频率的元组
                if heap[0][0] < freq:
                    heapq.heapreplace(heap, (freq, num))
            else : 
                heapq.heappush(heap, (freq, num))
        while heap :
            result.append(heapq.heappop(heap)[1])
        
        return result
