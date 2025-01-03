class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        O(log N)
        O(1)
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] <= nums[high]:  # min位于左侧上升沿
                high = mid
            else:  # min位于左侧上升沿与右侧上升沿之间
                low = mid + 1
        return nums[low]
