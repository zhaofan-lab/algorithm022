class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def MergeSort(left, right):
            if right <= left:
                return 0
            count = 0
            mid = (left + right) // 2
            count = MergeSort(left, mid) + MergeSort(mid + 1, right)
            temp = []
            i, j = left, left

            for k in range(mid+1, right+1):
                while i <= mid and nums[i] <= nums[k] * 2: i += 1
                while j <= mid and nums[j] < nums[k]:
                    temp.append(nums[j])
                    j += 1
                temp.append(nums[k])
                count += mid - i + 1

            while j <= mid:
                temp.append(nums[j])
                j += 1
            for i in range(right-left + 1):
                nums[left + i] = temp[i]

            return count
        if nums == []:
            return 0
        return MergeSort(0, len(nums) - 1)