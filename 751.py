###
线段树求区间最小值
###

from typing import (
    List,
)

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
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
        self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, left, right):
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        if start > right or end < left:
            return float('inf')
        if left <= start and right >= end:
            return self.tree[node]

        mid = (start + end) // 2
        left_val = self._query(2 * node + 1, start, mid, left, right)
        right_val = self._query(2 * node + 2, mid + 1, end, left, right)
        return min(left_val, right_val)

class Solution:
    """
    @param a: The prices [i]
    @param k: 
    @return: The ans array
    """
    def business(self, prices: List[int], k: int) -> List[int]:
        st = SegmentTree(prices)
        ans = []

        for i, price in enumerate(prices):
            min_price = st.query(i - k, i + k)
            ans.append(max(0, price - min_price))
        return ans




