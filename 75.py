###
二分法在非传统有序(山峰波动)的情况下应用
start + 1 < end确保只有三个数的时候才会进循环
###
class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid - 1] < nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid

        return start if nums[start] > nums[end] else end 
