###
线段树求区间最小值
###

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
            profit = price - st.query(st.root, max(0, i - k), min(len(prices) - 1, i + k))
            ans.append(profit)
        return ans 


class SegmentTree:
    class TreeNode:
        def __init__(self, start, end, val):
            self.start, self.end = start, end
            self.left, self.right = None, None
            self.val = val
    
    def __init__(self, nums):
        self.root = self.build(nums, 0, len(nums) - 1)
    
    def build(self, nums, start, end):
        if start == end:
            return SegmentTree.TreeNode(start, end, nums[start])
        
        root = SegmentTree.TreeNode(start, end, float('inf'))
        mid = (start + end) // 2
        root.left = self.build(nums, start, mid)
        root.right = self.build(nums, mid + 1, end)
        self.update_node_val(root)
        return root
    
    def update_node_val(self, root):
        root.val = float('inf')
        if root.left:
            root.val = min(root.val, root.left.val)
        if root.right:
            root.val = min(root.val, root.right.val)
    
    def query(self, root, start, end):
        if root.start == start and root.end == end:
            return root.val

        # ...1...start...3...end...2...
        mid = (root.start + root.end) // 2
        if mid < start:
            return self.query(root.right, start, end)
        elif mid >= end:
            return self.query(root.left, start, end)
        return min(self.query(root.left, start, mid), self.query(root.right, mid + 1, end))
