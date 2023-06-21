"""
拓扑排序(Topological Sorting)
"""

"""
bfs解法
将入度为0的点进queue
一次访问队列，计入result中，并将访问的neighbor入度减1
入度为0进队
最后依靠len(result) == 所有点 来判断是否存在拓扑序
"""

import collections
class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def find_order(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        if num_courses <= 0: return []
        if not prerequisites: return [i for i in range(num_courses)]

        indegree = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        for second, first in prerequisites:
            graph[first].append(second)
            indegree[second] += 1
        
        queue = collections.deque(node for node in range(num_courses) if indegree[node] == 0)
        result = []
        while queue:
            curt = queue.popleft()
            result.append(curt)
            for neighbor in graph[curt]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result if len(result) == num_courses else []


















