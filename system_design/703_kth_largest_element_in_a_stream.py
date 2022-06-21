from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap w/ K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


k = 3
nums = [4, 5, 8, 2]

kth = KthLargest(k, nums)
print(kth.minHeap)
res = kth.add(5)
print(kth.minHeap)
print(res)
