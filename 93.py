"""
分治法来判断是否是平衡二叉树

平衡二叉树（Balanced Binary Tree），也称为AVL树，是一种二叉树数据结构，它满足以下性质：对于任意一个节点，它的左子树和右子树的高度差不超过1，并且左子树和右子树也都是平衡二叉树。

O(n)
"""


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def is_balanced(self, root: TreeNode) -> bool:
        if not root: return True
        balanced, _ = self.helper(root)
        return balanced
    
    def helper(self, root):
        if not root: return (True, 0)

        left_is_balanced, left_height = self.helper(root.left)
        right_is_balanced, right_height = self.helper(root.right)

        if not left_is_balanced or not right_is_balanced:
            return (False, 0)
        if abs(left_height - right_height) > 1:
            return (False, 0)
        
        height = max(left_height, right_height) + 1
        return (True, height)
