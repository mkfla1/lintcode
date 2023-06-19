###
两次partition
O(n)
###
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sort_colors(self, nums: List[int]):
        if not nums: return []
        newStart = self.partition(nums, 0, len(nums) - 1, 0)
        _ = self.partition(nums, newStart, len(nums) - 1, 1)

    def partition(self, nums, start, end, pivot):
        if start >= end: return start + 1
        left, right = start, end

        while left <= right:
            while left <= right and nums[left] <= pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left > right: break
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return left

###
一次partition（三分）
在left,right的基础上再利用一个从start开始的i指针
根据nums[i]指的不同，分别处理
最终结果为
start...left...right...end
[left, right]闭区间都是1
###
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sort_colors(self, nums: List[int]):
        if not nums: return
        left, right = 0, len(nums) - 1
        i = 0

        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1