"""
给一组整数，请将其在原地按照升序排序。使用归并排序，快速排序，堆排序或者任何其他 O(n log n) 的排序算法。
"""


#快速排序
#平均时间复杂度O(nlogn)
class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers2(self, a: List[int]):
        if not a: return
        self.quickSort(a, 0, len(a) - 1)
    
    def quickSort(self, a, start, end):
        if start >= end: return
        left, right = start, end
        pivot = a[(start + end) // 2]

        while left <= right:
            while left <= right and a[left] < pivot:
                left += 1
            while left <= right and a[right] > pivot:
                right -= 1
            if left > right: break
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1
            
        self.quickSort(a, start, right)
        self.quickSort(a, left, end)

#归并排序 O(nlogn)
#需要额外占用O(n)空间，所以实战并不如快速排序
class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers2(self, a: List[int]):
        if not a: return
        tmp = [0] * len(a)
        self.mergeSort(a, 0, len(a) - 1, tmp)

    def mergeSort(self, nums, start, end, tmp):
        if start >= end: return
        mid = (start + end) // 2
        self.mergeSort(nums, start, mid, tmp)
        self.mergeSort(nums, mid + 1, end, tmp)
        self.merge(nums, start, end, tmp)
    
    def merge(self, nums, start, end, tmp):
        mid = (start + end) // 2
        index = start
        left, right = start, mid + 1

        while left <= mid and right <= end:
            if nums[left] <= nums[right]:
                tmp[index] = nums[left]
                left += 1
            else:
                tmp[index] = nums[right]
                right += 1
            index += 1
        
        while left <= mid:
            tmp[index] = nums[left]
            left += 1
            index += 1
        while right <= end:
            tmp[index] = nums[right]
            right += 1
            index += 1
        
        for i in range(start, end + 1):
            nums[i] = tmp[i]