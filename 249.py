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
    @param a: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def count_of_smaller_number_i_i(self, nums: List[int]) -> List[int]:
        # write your code here
        if not nums: return []
        st = SegmentTree(max(nums) + 1)
        ans = []

        for num in nums:
            st.update(num)
            ans.append(st.query(0, num - 1))
        return ans