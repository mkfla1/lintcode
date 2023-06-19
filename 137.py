"""
1. 复制点
2. 复制边

复制点的过程中，需要从一个点走遍所有点 -> bfs遍历
"""

"""
Definition for a UndirectedGraphNode:
class UndirectedGraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = []
"""


import collections
class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        if not node: return None

        old_to_newNode = self.copy_node(node)
        self.copy_edge(old_to_newNode)
        return old_to_newNode[node]
    
    def copy_node(self, node):
        old_to_newNode = {}
        queue = collections.deque([node])
        vis = set([node])

        while queue:
            node = queue.popleft()
            newNode = UndirectedGraphNode(node.label)
            old_to_newNode[node] = newNode

            for neighbor in node.neighbors:
                if neighbor in vis: continue
                vis.add(neighbor)
                queue.append(neighbor)
        return old_to_newNode
    
    def copy_edge(self, node_to_newNode):
        for node, newNode in node_to_newNode.items():
            for neighbor in node.neighbors:
                newNode.neighbors.append(node_to_newNode[neighbor])




