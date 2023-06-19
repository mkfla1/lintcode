###
先用倍增法确定end
然后去二分法找最左边的位置
O(logk)
###


class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        start, end = 0, 1
        while reader.get(end) <= target:
            end = end * 2
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            curt = reader.get(mid)
            if curt == target:
                end = mid
            elif curt < target:
                start = mid
            else:
                end = mid
        
        if reader.get(start) == target: return start
        if reader.get(end) == target: return end
        return -1