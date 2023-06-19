"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
bfs的分层遍历
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def level_order(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = collections.deque([root])
        ans = []

        while queue:
            level = []
            for _ in range(len(queue)):
                curt = queue.popleft()
                level.append(curt.val)
                if curt.left:
                    queue.append(curt.left)
                if curt.right:
                    queue.append(curt.right)
            ans.append(level)
        return ans
