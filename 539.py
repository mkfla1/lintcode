"""
同向双指针
快慢指针解决问题，最后将slow指针后不为0的全搞成0
"""
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def move_zeroes(self, nums: List[int]):
        if not nums or len(nums) <= 1: return
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        
        for i in range(slow, len(nums)):
            if nums[i] != 0: 
                nums[i] = 0
