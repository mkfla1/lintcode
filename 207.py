###
线段树
###

class TreeNode:
    def __init__(self, start, end, val):
        self.start, self.end = start, end
        self.left, self.right = None, None
        self.sum = val

class SegmentTree:
    def __init__(self, nums):
        self.root = self.build(nums, 0, len(nums) - 1)
    
    def build(self, nums, start, end):
        if start > end: return None
        if start == end:
            return TreeNode(start, end, nums[start])
        
        node = TreeNode(start, end, 0)
        mid = start + (end - start) // 2
        node.left = self.build(nums, start, mid)
        node.right = self.build(nums, mid + 1, end)

        self.update_sum(node)
        return node
    
    def update_sum(self, node):
        node.sum = 0
        if node.left:
            node.sum += node.left.sum
        if node.right:
            node.sum += node.right.sum
    
    def query(self, root, start, end):
        if root.start == start and root.end == end:
            return root.sum
        mid = root.start + (root.end - root.start) // 2
        if mid < start:
            return self.query(root.right, start, end)
        if mid >= end:
            return self.query(root.left, start, end)
        if start <= mid < end:
            return self.query(root.left, start, mid) + self.query(root.right, mid + 1, end)
        return 0
    
    def update(self, root, index, val):
        if not root.start <= index <= root.end: return
        if root.start == index and root.end == index:
            root.sum = val
            return
        
        mid = root.start + (root.end - root.start) // 2
        if mid < index:
            self.update(root.right, index, val)
        else:
            self.update(root.left, index, val)
        self.update_sum(root)
        return
        
class Solution:
    def __init__(self, nums):
        self.st = SegmentTree(nums)
            
    def query(self, start, end):
        return self.st.query(self.st.root, start, end)

    def modify(self, index, value):
        self.st.update(self.st.root, index, value)