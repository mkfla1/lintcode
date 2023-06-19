###
二分法
将两种特殊情况判断下
1. mid在下半, target却在上半
2. mid在上半，target却在下半
剩下的就是通用情况喽
O(logn)
###
class Solution:
    """
    @param a: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target: return mid

            if nums[mid] <= nums[-1] and target > nums[-1]:
                end = mid
                continue
            if nums[mid] > nums[-1] and target <= nums[-1]:
                start = mid
                continue
            if nums[mid] < target:
                start = mid
            else:
                end = mid
                
        if nums[start] == target: return start
        if nums[end] == target: return end
        return -1

