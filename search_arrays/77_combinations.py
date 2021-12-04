class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        O(N choose M)
        """
        res = []
        self.helper(range(1, n + 1), k, res, [])
        return res

    def helper(self, array, k, res, path):
        if k > len(array):
            return
        if k == 0:
            res.append(path)
        else:
            self.helper(array[1:], k - 1, res, path + [array[0]])
            self.helper(array[1:], k, res, path)
