# 二叉树用分治法来解决
# 处理时要分析三种情况
# 要求的时路径长度：总点数 - 1

from lintcode import TreeNode

class Solution:
    """
    计算二叉树的直径长度
    """
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        _, diameter = self.helper(root)
        return diameter
    
    def helper(self, root):
        """
        递归计算以当前节点为根的子树的深度和直径长度
        """
        if not root:
            return 0, 0
        
        left_height, left_diameter = self.helper(root.left)
        right_height, right_diameter = self.helper(root.right)
        height = 1 + max(left_height, right_height)
        diameter = max(left_height + right_height, left_diameter, right_diameter)
        return height, diameter
