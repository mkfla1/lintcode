###
线段树求区间最小值
###

from typing import (
    List,
)

class SegmentTree:
    class TreeNode:
        def __init__(self, start, end, val):
            self.start, self.end = start, end
            self.left, self.right = None, None
            self.val = val
    
    def __init__(self, nums):
        self.root = self.build(nums, 0, len(nums) - 1)
    
    def build(self, nums, start, end):
        root = self.TreeNode(start, end, float('inf'))
        if start == end:
            root.val = nums[start]
            return root
        
        mid = (start + end) // 2
        root.left = self.build(nums, start, mid)
        root.right = self.build(nums, mid + 1, end)
        root.val = min(root.left.val, root.right.val)
        return root
    
    def query(self, start, end, root=None):
        if root is None:
            root = self.root
        
        if root.start >= start and root.end <= end:
            return root.val
        if root.start > end or root.end < start:
            return float('inf')
        return min(self.query(start, end, root.left), self.query(start, end, root.right))

class Solution:
    """
    @param a: The prices [i]
    @param k: 
    @return: The ans array
    """
    def business(self, prices: List[int], k: int) -> List[int]:
        if not prices:
            return []
        
        st = SegmentTree(prices)
        ans = []
        for i, price in enumerate(prices):
            min_price = st.query(i - k, i + k)
            ans.append(price - min_price)
        return ans

