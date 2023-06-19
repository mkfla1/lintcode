###
OOXX型二分
求最小值我们用右端点作为判断
求最大值时我们用左端点

判断依据你就看不旋转一条斜直线时的情况就好了
不能包含重复元素，否则变成O(n)算法，0000010000比如千里寻1的情况
###
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def find_min(self, nums: List[int]) -> int:
        if not nums: raise Exception("数不够")
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= nums[-1]:
                end = mid
            else:
                start = mid
        return min(nums[start], nums[end])
