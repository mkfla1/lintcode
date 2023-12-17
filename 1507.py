###
前缀和+单调队列
O(n)
###

import collections
class Solution:
    """
    @param a: the array
    @param k: sum
    @return: the length
    """
    def shortest_subarray(self, nums: List[int], k: int) -> int:
        if not nums: return -1
        # 计算前缀和
        prefix_sum = [0]
        for val in nums:
            prefix_sum.append(prefix_sum[-1] + val)

        # 初始化单调队列和结果变量
        min_length = float('inf')
        mq = collections.deque()

        for i in range(len(prefix_sum)):
            # 检查并更新最短子数组长度
            while mq and prefix_sum[i] - prefix_sum[mq[0]] >= k:
                min_length = min(min_length, i - mq.popleft())
            # 维护单调队列    
            while mq and prefix_sum[i] <= prefix_sum[mq[-1]]:
                mq.pop()
                
            mq.append(i)
        
        return min_length if min_length != float('inf') else -1


###
前缀和暴力法
O(n^2)
###

class Solution:
    """
    @param a: the array
    @param k: sum
    @return: the length
    """
    def shortest_subarray(self, nums: List[int], k: int) -> int:
        if not nums: return -1
        prefix_sum = self.get_prefix_sum(nums)
        min_length = float('inf')

        for right in range(1, len(prefix_sum)):
            for left in range(0, right):
                if prefix_sum[right] - prefix_sum[left] >= k:
                    min_length = min(min_length, right - left)
        return min_length if min_length != float('inf') else -1
    
    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for val in nums:
            prefix_sum.append(prefix_sum[-1] + val)
        return prefix_sum    
        
###
线段树
O(nlogn)
把前缀和离散化，不然线段树体积太大了
线段树区间用的是 离散化的前缀和，存储的是ps中的index
每次求st.query(0, ps_to_discrete[ps[i] - k])中的最大index, 即目标start
i - start就是长度
###
from typing import (
    List,
)

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [-1] * (4 * n)
    
    def query(self, left, right):
        return self._query(0, 0, self.n - 1, left, right)
    
    def _query(self, node, start, end, left, right):
        if start > right or end < left:
            return -1
        if start >= left and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_val = self._query(2 * node + 1, start, mid, left, right)
        right_val = self._query(2 * node + 2, mid + 1, end, left, right)
        return max(left_val, right_val)
    
    def update(self, index, val):
        self._update(0, 0, self.n - 1, index, val)
    
    def _update(self, node, start, end, index, val):
        if start == end:
            self.tree[node] = val
            return
        
        mid = (start + end) // 2
        if index <= mid:
            self._update(2 * node + 1, start, mid, index, val)
        else:
            self._update(2 * node + 2, mid + 1, end, index, val)
        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])


class Solution:
    """
    @param a: the array
    @param k: sum
    @return: the length
    """
    def shortest_subarray(self, nums: List[int], k: int) -> int:
        if not nums: returun -1

        ps, ps_to_discrete = self.setup(nums, k)
        st = SegmentTree(len(ps_to_discrete))
        min_length = float('inf')

        for i in range(len(ps)):
            start = st.query(0, ps_to_discrete[ps[i] -  k])
            if start != -1:
                min_length = min(min_length, i - start)
            st.update(ps_to_discrete[ps[i]], i)
        
        return min_length if min_length != float('inf') else -1
    
    def setup(self, nums, k):
        ps = [0]
        for num in nums:
            ps.append(num + ps[-1])
        
        ps_set = set()
        for num in ps:
            ps_set.add(num)
            ps_set.add(num - k)
        
        ps_to_discrete = {val: i for i, val in enumerate(sorted(list(ps_set)))}
        return ps, ps_to_discrete


###
二分答案+堆
O(n(logn)^2)
###
from typing import (
    List,
)

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
        heappop(self.heap)

    def delete(self, index):
        self.deleted_set.add(index)

    def is_empty(self):
        return not bool(self.heap)

class Solution:
    """
    @param a: the array
    @param k: sum
    @return: the length
    """
    def shortest_subarray(self, nums: List[int], k: int) -> int:
        if not nums: return -1

        ps = [0]
        for num in nums:
            ps.append(num + ps[-1])

        start, end = 1, len(nums)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.check_valid(ps, mid, k):
                end = mid
            else:
                start = mid
        
        if self.check_valid(ps, start, k): return start
        if self.check_valid(ps, end, k): return end
        return -1

    def check_valid(self, ps, length, k):
        heap = Heap()
        heap.push(0, 0)

        for i in range(1, len(ps)):
            if i >= length:
                heap.delete(i - length - 1)
            min_ps, _ = heap.top()
            if ps[i] - min_ps >= k:
                return True
            heap.push(ps[i], i)
        return False

###
二分答案+线段树
O(n(logn)^2)
###
from typing import (
    List,
)

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        #设置初始值
        self.tree = [float('inf')] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, node, start, end):
        if start > end: return
        
        if start == end:
            self.tree[node] = nums[start]
            return

        mid = (start + end) // 2
        self.build(nums, 2 * node + 1, start, mid)
        self.build(nums, 2 * node + 2, mid + 1, end)
        #根据线段树类型更改
        self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, index, val):
        self._update(0, 0, self.n - 1, index, val)

    def _update(self, node, start, end, index, val):
        if start == end:
            self.tree[node] = val
            return

        mid = (start + end) // 2
        if index <= mid:
            self._update(2 * node + 1, start, mid, index, val)
        else:
            self._update(2 * node + 2, mid + 1, end, index, val)
        #根据线段树类型更改
        self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, left, right):
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        #不存在，返回初始值
        if start > right or end < left:
            return float('inf')

        if left <= start and right >= end:
            return self.tree[node]

        mid = (start + end) // 2
        left_val = self._query(2 * node + 1, start, mid, left, right)
        right_val = self._query(2 * node + 2, mid + 1, end, left, right)
        #根据线段树类型更改
        return min(left_val, right_val)

class Solution:
    """
    @param a: the array
    @param k: sum
    @return: the length
    """
    def shortest_subarray(self, nums: List[int], k: int) -> int:
        if not nums: return -1

        ps = [0]
        for num in nums:
            ps.append(num + ps[-1])
        st = SegmentTree(ps)

        start, end = 1, len(nums)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.check_valid(ps, mid, k, st):
                end = mid
            else:
                start = mid
        
        if self.check_valid(ps, start, k, st): return start
        if self.check_valid(ps, end, k, st): return end
        return -1

    def check_valid(self, ps, length, k, st):
        for i in range(1, len(ps)):
            min_ps = st.query(i - length, i)
            if ps[i] - min_ps >= k:
                return True
        return False


        

