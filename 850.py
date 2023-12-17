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
    @param schedule: a list schedule of employees
    @return: Return a list of finite intervals 
    """
    def employee_free_time(self, schedule: List[List[int]]) -> List[Interval]:
        if not schedule: return []
        events = []
        for employee in schedule:
            for i in range(0, len(employee), 2):
                if i + 1 == len(employee): continue
                events.append((employee[i], 'start'))
                events.append((employee[i + 1], 'end'))
        events.sort(key=lambda x: (x[0], -1 if x[1] == 'start' else 1))

        active_intervals = 0
        ans = []
        last_end = float('-inf')

        for position, event_type in events:
            if event_type == 'start':
                if active_intervals == 0 and last_end != float('-inf'):
                    ans.append(Interval(last_end, position))
                active_intervals += 1
            else:
                active_intervals -= 1
                last_end = max(last_end, position)
        return ans
            
