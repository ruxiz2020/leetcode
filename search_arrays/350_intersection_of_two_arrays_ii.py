class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        l1, l2 = 0, 0
        N1, N2 = len(nums1), len(nums2)
        res = []
        while l1 != N1 and l2 != N2:
            if nums1[l1] == nums2[l2]:
                res.append(nums1[l1])
                l1 += 1
                l2 += 1
            elif nums1[l1] < nums2[l2]:
                l1 += 1
            else:
                l2 += 1
        return res
