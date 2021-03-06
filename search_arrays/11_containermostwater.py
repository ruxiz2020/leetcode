class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        O(n)
        """
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans


if __name__ == '__main__':

    height = [1,8,6,2,5,4,8,3,7]

    ss = Solution()
    res = ss.maxArea(height)

    print(res)
