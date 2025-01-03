import heapq
from typing import List


class Solution:
    """O(N + k LOG(N))
    O(N + K)
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            pts.append([dist, x, y])

        res = []
        heapq.heapify(pts) #O(N)
        print(pts)
        for i in range(k):
            dist, x, y = heapq.heappop(pts) # O(log N)
            res.append([x, y])
        return res

points = [[3,3],[5,-1],[-2,4]]; k = 2

ss = Solution()
res = ss.kClosest(points, k)
print(res) #[[3, 3], [-2, 4]]
