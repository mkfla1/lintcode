"""
遍历法
采用前序遍历
O(n)时间复杂度

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
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
             we will sort your return value in output
    """
    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        if not root: return []
        paths = []
        self.traverse(root, [], paths)
        return paths
    
    def traverse(self, root, curt, paths):
        if not root: return

        curt.append(root)
        if not root.left and not root.right:
            path = "->".join(str(node.val) for node in curt)
            paths.append(path)
            curt.pop()
            return
        
        self.traverse(root.left, curt, paths)
        self.traverse(root.right, curt, paths)
        curt.pop() 
