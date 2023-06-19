###
对所求的答案范围进行二分
然后写个子函数进行条件判断
O(log答案范围)
###
class Solution:
    """
    @param l: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def wood_cut(self, l: List[int], k: int) -> int:
        if not l: return 0
        start = 1
        end = max(l)

        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.can_chop(l, mid, k):
                start = mid
            else:
                end = mid

        if self.can_chop(l, end, k): return end
        if self.can_chop(l, start, k): return start
        return 0
    
    def can_chop(self, l, target, k):
        number = 0

        for wood_length in l:
            number += wood_length // target
            if number >= k: return True
        return False

