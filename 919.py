###
扫描线算法
###

from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        events = []
        for interval in intervals:
            events.append((interval.start, 'start'))
            events.append((interval.end, 'end'))
        events.sort()

        active_intervals = 0
        room = 0

        for position, event_type in events:
            if event_type == 'start':
                active_intervals += 1
                room = max(room, active_intervals)
            else:
                active_intervals -= 1
        return room


###
扫描线算法 + 堆来排序
###
import heapq
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        events = []
        for interval in intervals:
            heapq.heappush(events, (interval.start, 'start'))
            heapq.heappush(events, (interval.end, 'end'))

        active_intervals = 0
        room = 0

        while events:
            position, event_type = heapq.heappop(events)
            if event_type == 'start':
                active_intervals += 1
                room = max(room, active_intervals)
            else:
                active_intervals -= 1
        return room