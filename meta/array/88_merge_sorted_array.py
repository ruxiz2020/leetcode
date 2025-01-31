class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        O(m + n)
        O(1)
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n -1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]


nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3

ss = Solution()
res = ss.merge(nums1, m, nums2, n)
# [1, 2, 2, 3, 5, 6]
print(nums1)
