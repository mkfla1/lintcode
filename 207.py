###
线段树
###

class SegmentTree:
    class TreeNode:
        def __init__(self, start, end, val):
            self.start, self.end = start, end
            self.left, self.right = None, None
            self.val = val
    
    def __init__(self, nums):
        self.root = self.build(nums, 0, len(nums) - 1)
    
    def build(self, nums, start, end):
        if start > end: return None
        root = self.TreeNode(start, end, 0)
        
        if start == end:
            root.val = nums[start]
            return root
        
        mid = (start + end) // 2
        root.left = self.build(nums, start, mid)
        root.right = self.build(nums, mid + 1, end)
        root.val = root.left.val + root.right.val
        return root
    
    def query(self, start, end, root=None):
        if root is None:
            root = self.root
        
        if root.start >= start and root.end <= end:
            return root.val
        if root.start > end or root.end < start:
            return 0
        return self.query(start, end, root.left) + self.query(start, end, root.right)
    
    def update(self, index, val, root=None):
        if root is None:
            root = self.root
        
        if root.start == index and root.end == index:
            root.val = val
            return
        
        mid = (root.start + root.end) // 2
        if mid < index:
            self.update(index, val, root.right)
        else:
            self.update(index, val, root.left)
        root.val = root.left.val + root.right.val

class Solution:
    """
    @param: A: An integer array
    """
    def __init__(self, A):
        self.st = SegmentTree(A)

    """
    @param: start: An integer
    @param: end: An integer
    @return: The sum from start to end
    """
    def query(self, start, end):
        # write your code here
        return self.st.query(start, end)

    """
    @param: index: An integer
    @param: value: An integer
    @return: nothing
    """
    def modify(self, index, value):
        # write your code here
        self.st.update(index, value)