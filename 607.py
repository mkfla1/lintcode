###
哈希表的方式
O(1)时间add
O(n)时间find
###


class TwoSum:
    def __init__(self):
        self.valToCount = {}

    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        self.valToCount[number] = self.valToCount.get(number, 0) + 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        for op1 in self.valToCount.keys():
            op2 = value - op1
            if op2 == op1:
                if self.valToCount[op1] > 1:
                    return True
            else:
                if op2 in self.valToCount:
                    return True
        return False

###
借助有序数组+双指针
O(logn) add
O(n) find
###
from sortedcontainers import SortedList
class TwoSum:
    def __init__(self):
        self.sl = SortedList()

    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        self.sl.add(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        left, right = 0, len(self.sl) - 1
        while left < right: 
            curt = self.sl[left] + self.sl[right]
            if curt == value: return True
            if curt < value: 
                left += 1
            else:
                right -= 1
        return False