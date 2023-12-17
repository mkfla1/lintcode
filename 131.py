###
扫描线 + 最大堆辅助
扫描线记录(position, height, state, idx)
position升序
height降序
state, 'start'优先
idx不参与排序
idx用来让堆实现O(logn)的lazy删除

轮廓变化取决于堆里的最大高度变化，或者归0（堆空了）的时候
###

from typing import (
    List,
)

from heapq import heappush, heappop
class Heap:
    def __init__(self):
        self.heap = []
        self.deleted_set = set()
    
    def push(self, val, idx):
        heappush(self.heap, (val, idx))
    
    def _lazy_delete(self):
        while self.heap and self.heap[0][1] in self.deleted_set:
            _, idx = heappop(self.heap)
            self.deleted_set.remove(idx)
    
    def delete(self, idx):
        self.deleted_set.add(idx)
    
    def top(self):
        self._lazy_delete()
        return self.heap[0][0]
    
    def is_empty(self):
        self._lazy_delete()
        return not bool(self.heap)

class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """
    def building_outline(self, buildings: List[List[int]]) -> List[List[int]]:
        # write your code here
        if not buildings: return []
        events = []
        for idx, (start, end, height) in enumerate(buildings):
            events.append((start, height, 'start', idx))
            events.append((end, height, 'end', idx))
        events.sort(key=lambda x: (x[0], -x[1], -1 if x[2] == 'start' else 1))

        max_heap = Heap()
        ans = []
        prev, prev_height = 0, 0

        for position, height, state, idx in events:
            if max_heap.is_empty():
                prev = position
                prev_height = height
            
            if state == 'start':
                max_heap.push(-height, idx)
            else:
                max_heap.delete(idx)
            
            curt = 0 if max_heap.is_empty() else -max_heap.top()
            if curt == 0 or curt != prev_height:
                if position != prev:
                    ans.append([prev, position, prev_height])
                prev = position
                prev_height = curt

        return ans
