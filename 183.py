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
    def wood_cut(self, woods: List[int], k: int) -> int:
        if k == 0: return max(woods)
        if not woods: return 0

        start, end = 1, max(woods)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.check_valid(mid, woods, k):
                start = mid
            else:
                end = mid
        
        if self.check_valid(end, woods, k): return end
        if self.check_valid(start, woods, k): return start
        return 0
    
    def check_valid(self, length, woods, k):
        segment = 0

        for wood in woods:
            segment += wood // length
            if segment >= k:
                return True
        return False