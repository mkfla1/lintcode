from typing import (
    List,
)
from lintcode import (
    Point,
)

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""
import collections
DIRECTION = [(1,2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
WALL = 1

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """

    def shortest_path(self, grid: List[List[bool]], source: Point, destination: Point) -> int:
        if not grid or not grid[0]: return -1
        source = (source.x, source.y)
        destination = (destination.x, destination.y)
        if source == destination: return 0

        point_to_distance = {source: 0}
        queue = collections.deque([source])

        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTION:
                nx, ny = x + dx, y + dy
                if not self.is_valid(nx, ny, grid, point_to_distance):
                    continue
                point_to_distance[(nx, ny)] = point_to_distance[(x, y)] + 1
                if (nx, ny) == destination:
                    return point_to_distance[(nx, ny)]
                queue.append((nx, ny))
        return -1
    
    def is_valid(self, x, y, grid, point_to_distance):
        if (x, y) in point_to_distance:
            return False
        if not 0 <= x < len(grid):
            return False
        if not 0 <= y < len(grid[0]):
            return False
        if grid[x][y] == WALL:
            return False
        return True



















