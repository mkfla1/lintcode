"""
借助哈希表
O(n)空间和时间
"""

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers: return []
        numToIndex = {}
        for i in range(len(numbers)):
            val = target - numbers[i]
            if val in numToIndex:
                return [numToIndex[val], i]
            numToIndex[numbers[i]] = i
        return []




"""
排序后双指针
O(n)时间
O(nlogn)空间
"""
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        valIndexPair = [(numbers[index], index) for index in range(len(numbers))]
        valIndexPair.sort()

        left, right = 0, len(valIndexPair) - 1
        while left < right:
            curt = valIndexPair[left][0] + valIndexPair[right][0]
            if curt == target:
                return sorted([valIndexPair[left][1], valIndexPair[right][1]])
            if curt < target:
                left += 1
            else:
                right -= 1
        return []