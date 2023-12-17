###
栈+最大堆+lazy_delete
###

from heapq import heappush, heappop
class Heap:
    def __init__(self):
        self.heap = []
        self.deleted_set = set()

    def push(self, val, index):
        heappush(self.heap, (val, index))

    def _lazy_delete(self):
        while self.heap and self.heap[0][1] in self.deleted_set:
            _, index = heappop(self.heap)
            self.deleted_set.remove(index)

    def top(self):
        self._lazy_delete()
        return self.heap[0]

    def pop(self):
        self._lazy_delete()
        return heappop(self.heap)

    def delete(self, index):
        self.deleted_set.add(index)

    def is_empty(self):
        self._lazy_delete()
        return not bool(self.heap)

class MaxStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.max_heap = Heap()
        self.idx = 0
        self.deleted_set = set()
    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.stack.append((x, self.idx))
        self.max_heap.push(-x, -self.idx)
        self.idx += 1

    def _lazy_delete(self):
        while self.stack and self.stack[-1][1] in self.deleted_set:
            _, index = self.stack.pop()
            self.deleted_set.remove(index)
    
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        self._lazy_delete()
        val, index = self.stack.pop()
        self.max_heap.deleted_set.add(-index)
        return val

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        self._lazy_delete()
        return self.stack[-1][0]

    """
    @return: An integer
    """
    def peekMax(self):
        # write your code here
        val, _ = self.max_heap.top()
        val = -val
        return val

    """
    @return: An integer
    """
    def popMax(self):
        # write your code here
        val, index = self.max_heap.pop()
        val, index = -val, -index
        self.deleted_set.add(index)
        return val



