"""
SPFA
"""

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
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortest_distance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # write your code here
        start, destination = tuple(start), tuple(destination)

        distance = [[float('inf')] * len(maze[0]) for _ in range(len(maze))]
        distance[start[0]][start[1]] = 0
        queue = collections.deque([start])
        in_queue = set([start])

        while queue:
            curt = queue.popleft()
            in_queue.remove(curt)

            for dx, dy in DIRECTIONS:
                nx, ny = curt[0] + dx, curt[1] + dy
                move = 1
                while 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == EMPTY:
                    nx += dx
                    ny += dy
                    move += 1
                nx -= dx
                ny -= dy
                move -= 1

                new_distance = distance[curt[0]][curt[1]] + move
                if new_distance < distance[nx][ny]:
                    distance[nx][ny] = new_distance
                    if (nx, ny) not in in_queue:
                        in_queue.add((nx, ny))
                        queue.append((nx, ny))
        
        return distance[destination[0]][destination[1]] if distance[destination[0]][destination[1]] != float('inf') else -1


"""
dijkstra算法
利用有限队列
"""
from typing import (
    List,
)
import heapq

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
WALL = 1
EMPTY = 0

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortest_distance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # write your code here
        start, destination = tuple(start), tuple(destination)

        distance = [[float('inf')] * len(maze[0]) for _ in range(len(maze))]
        distance[start[0]][start[1]] = 0
        queue = [(0, start)]

        while queue:
            curt_move, curt = heapq.heappop(queue)
            if curt == destination: return curt_move
            if curt_move > distance[destination[0]][destination[1]]: continue

            for dx, dy in DIRECTIONS:
                nx, ny = curt[0] + dx, curt[1] + dy
                move = 0
                while 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == EMPTY:
                    nx += dx
                    ny += dy
                    move += 1
                nx -= dx
                ny -= dy

                new_distance = curt_move + move
                if new_distance < distance[nx][ny]:
                    distance[nx][ny] = new_distance
                    heapq.heappush(queue, (new_distance, (nx, ny)))
        
        return -1





