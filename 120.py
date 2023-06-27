###
bfs 求简单图最短路径
###
import collections
class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: An integer
    """
    def ladder_length(self, start: str, end: str, dict: Set[str]) -> int:
        dict.add(end)
        queue = collections.deque(collections.deque([start]))
        visited = set([start])
        graph = {}
        length = 0

        while queue:
            length += 1
            for _ in range(len(queue)):
                curt = queue.popleft()
                self.lazy_load(curt, graph, dict)
                for neighbor in graph[curt]:
                    if neighbor == end:
                        return length + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        return 0
    
    def lazy_load(self, curt, graph, dict):
        if curt in graph: return
        letters = "abcdefghijklmnopqrstuvwxyz"
        
        graph[curt] = []
        for i in range(len(curt)):
            for letter in letters:
                if letter == curt[i]:
                    continue
                new_word = curt[:i] + letter + curt[i + 1:]
                if new_word in dict:
                    graph[curt].append(new_word)
        return

###
双向bfs
###
import collections
class Solution:
    def ladder_length(self, start: str, end: str, dict: Set[str]) -> int:
        dict.add(start)
        dict.add(end)
        forward_queue = collections.deque(collections.deque([start]))
        forward_visited = set([start])
        backward_queue = collections.deque(collections.deque([end]))
        backward_visited = set([end])
        graph = {}
        length = 1

        while forward_queue and backward_queue:
            length += 1
            if self.bfs(forward_queue, forward_visited, backward_visited, graph, dict):
                return length
            length += 1
            if self.bfs(backward_queue, backward_visited, forward_visited, graph, dict):
                return length
            
        return 0
    
    def lazy_load(self, curt, graph, dict):
        if curt in graph: return
        letters = "abcdefghijklmnopqrstuvwxyz"
        
        graph[curt] = []
        for i in range(len(curt)):
            for letter in letters:
                if letter == curt[i]:
                    continue
                new_word = curt[:i] + letter + curt[i + 1:]
                if new_word in dict:
                    graph[curt].append(new_word)
        return
    
    def bfs(self, queue, visited, reverse_visited, graph, dict):
        for _ in range(len(queue)):
            curt = queue.popleft()
            self.lazy_load(curt, graph, dict)
            for neighbor in graph[curt]:
                if neighbor in reverse_visited:
                    return True
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
        return False
