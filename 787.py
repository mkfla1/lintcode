from typing import (
    List,
)

import collections

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
WALL = 1
EMPTY = 0

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def has_path(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # write your code here
        start = (start[0], start[1])
        destination = (destination[0], destination[1])

        queue = collections.deque([start])
        vis = set([start])

        while queue:
            curt = queue.popleft()
            if curt == destination: return True
            for dx, dy in DIRECTIONS:
                new_location = self.move(curt, dx, dy, maze)
                if new_location not in vis:
                    vis.add(new_location)
                    queue.append(new_location)
        return False
    
    def move(self, curt, dx, dy, maze):
        ox, oy = curt[0], curt[1]

        while True:
            x, y = ox + dx, oy + dy
            if not (0 <= x < len(maze) and 0 <= y < len(maze[0])):
                break
            if maze[x][y] == WALL:
                break
            ox, oy = x, y
        return (ox, oy)


        
                

