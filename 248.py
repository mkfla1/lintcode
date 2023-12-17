###
数据量不大时，直接用排序+二分搜索即可
O(nlogn + mlogn)
###

from typing import (
    List,
)

import bisect
class Solution:
    """
    @param a: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def count_of_smaller_number(self, nums: List[int], queries: List[int]) -> List[int]:
        # write your code here
        nums = sorted(nums)
        ans = []

        for query in queries:
            ans.append(bisect.bisect_left(nums, query))
        return ans


###
数据量很大时就需要线段树了
由于数值范围Range不大，0 到 10000，Olog(10000)在线段树其实就是个100的常数了
O(nlog(range) + mlog(range)) -> O(n + m)
###
from typing import (
    List,
)

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
    
    def update(self, index):
        self._update(0, 0, self.n - 1, index)
    
    def _update(self, node, start, end, index):
        if start == end:
            self.tree[node] += 1
            return
        
        mid = (start + end) // 2
        if index <= mid:
            self._update(2 * node + 1, start, mid, index)
        else:
            self._update(2 * node + 2, mid + 1, end, index)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def query(self, left, right):
        return self._query(0, 0, self.n - 1, left, right)
    
    def _query(self, node, start, end, left, right):
        if start > right or end < left:
            return 0
        if start >= left and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_val = self._query(2 * node + 1, start, mid, left, right)
        right_val = self._query(2 * node + 2, mid + 1, end, left, right)
        return left_val + right_val

class Solution:
    """
    @param a: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def count_of_smaller_number(self, nums: List[int], queries: List[int]) -> List[int]:
        if not nums: return [0] * len(queries)
        st = SegmentTree(max(nums) + 1)
        for num in nums:
            st.update(num)
        
        ans = []
        for query in queries:
            ans.append(st.query(0, query - 1))
        return ans
