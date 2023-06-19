###
二分法+背向双指针
二分法找到第一个>=target的位置作为right指针, 
left = right - 1， 开始背向双指针
涉及复杂的判断，写一个函数，让一切变得轻松
O(logn + k)
###


import bisect

class Solution:
    """
    @param a: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def k_closest_numbers(self, nums: List[int], target: int, k: int) -> List[int]:
        right = bisect.bisect_left(nums, target)
        left = right -1

        ans = []
        for _ in range(k):
            if self.left_is_better(nums, left, right, target):
                ans.append(nums[left])
                left -= 1
            else:
                ans.append(nums[right])
                right += 1
        return ans
    
    def left_is_better(self, nums, left, right, target):
        if right >= len(nums): return True
        if left < 0: return False
        return target - nums[left] <= nums[right] - target


###
自己写bisect_left
### 
def bisect_left(self, nums, target):
    start, end = 0, len(nums) - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            end = mid
        elif nums[mid] < target:
            start = mid
        else:
            end = mid
    
    if nums[start] >= target: return start
    if nums[end] >= target: return end
    return end + 1


