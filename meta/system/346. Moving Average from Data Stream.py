import collections


class MovingAverage:
    """
    O(1)
    O(size)
    """
    def __init__(self, size: int):
        self.size = size
        self.sum = 0
        self.q = collections.deque()

    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.sum -= self.q.popleft()
        self.sum += val
        self.q.append(val)
        return self.sum / len(self.q)

ma = MovingAverage(3)

res = ma.next(1)
print(res) # 1
res = ma.next(10)
print(res) # 5.5
