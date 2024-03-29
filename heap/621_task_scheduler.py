from typing import List
import heapq

from collections import Counter, deque

class Solution:
    '''O(m * n)'''
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        print(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,  q.popleft()[0])
        return time


if __name__ == '__main__':

    tasks = ["A","A","A","B","B","B", "C"]
    n = 2

    ss = Solution()
    res = ss.leastInterval(tasks, n)

    print(res)
