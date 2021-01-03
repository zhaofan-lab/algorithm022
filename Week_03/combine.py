class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrace(curr_res, index):
            if len(curr_res)==k:
                result.append(curr_res[:])
                return
            for i in range(index,n + 1):
                curr_res.append(i)
                backtrace(curr_res,i+1)
                curr_res.pop()
        
        if n==0 or k==0:
            return result
        cur_res = []
        backtrace(cur_res, 1)
        return result