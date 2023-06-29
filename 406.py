###
同向双指针
###
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimum_size(self, nums: List[int], s: int) -> int:
        if not nums: return -1

        slow = 0
        min_size = float('inf')
        curt_sum = 0

        for fast in range(len(nums)):
            curt_sum += nums[fast]

            while slow <= fast and curt_sum >= s:
                min_size = min(min_size, fast - slow + 1)
                curt_sum -= nums[slow]
                slow += 1
        return min_size if min_size != float('inf') else -1


