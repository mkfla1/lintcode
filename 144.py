###
给出一个含有正整数和负整数的数组，重新排列成一个正负数交错的数组。


O(n)
1.先数出来正负数各有多少个
2.partion将多的放在左半边
3.接下来利用reverse型相向双指针，swag时有两种情况决定right的起点
    +++--- -> +-+-+-  right = len(a) - 2
    ++++--- -> +-+-+-+ right = len(a) - 1
###
class Solution:
    """
    @param a: An integer array.
    @return: nothing
    """
    def rerange(self, a: List[int]):
        if not a or len(a) <= 1: return
        positive, negtive = self.count(a)
        flag = 1 if positive >= negtive else -1
        
        self.partition(a, 0, len(a) - 1, flag)
        self.swag(a, positive == negtive)
    
    def count(self, a):
        positive, negtive = 0, 0
        for val in a:
            if val >= 0:
                positive += 1
            else:
                negtive += 1
        return (positive, negtive)
    
    def partition(self, a, start, end, flag):
        if start >= end: return
        left, right = start, end
        pivot = a[(start + end) // 2]

        while left <= right:
            while left <= right and a[left] * flag > 0:
                left += 1
            while left <= right and a[right] * flag < 0:
                right -= 1
            if left > right: break
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1
    
    def swag(self, a, isSameCount):
        left = 1
        right = len(a) - 2 if isSameCount else len(a) - 1
        while left <= right:
            a[left], a[right] = a[right], a[left]
            left += 2
            right -=2
    


