###
贪心
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
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals: return []
        intervals = sorted(intervals, key=lambda x: x.start)
        ans = []

        for interval in intervals:
            if not ans or interval.start > ans[-1].end:
                ans.append(interval)
            else:
                ans[-1].end = max(ans[-1].end, interval.end)
        return ans


###
扫描线
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
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals: return []
        events = []
        for interval in intervals:
            events.append((interval.start, 'start'))
            events.append((interval.end, 'end'))
        events.sort(key=lambda x:(x[0], -1 if x[1] == 'start' else 1))
        
        ans = []
        active_intervals = 0
        start = 0

        for position, event_type in events:
            if event_type == 'start':
                if active_intervals == 0:
                    start = position
                active_intervals += 1
            else:
                active_intervals -= 1
                if active_intervals == 0:
                    ans.append(Interval(start, position))

        return ans
