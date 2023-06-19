###
找到数组中第K大的元素，N远大于K。请注意你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素
###

#基于快速排序，但是只需要走一条分支 -> O(n+ n/2 + n/4 + ...) = O(n)
class Solution:
    """
    @param nums: an integer unsorted array
    @param k: an integer from 1 to n
    @return: the kth largest element
    """
    def kth_largest_element2(self, nums: List[int], k: int) -> int:
        ans = self.quickSelect(nums, 0, len(nums) - 1, k)
        return ans
    
    def quickSelect(self, nums, start, end, k):
        if start >= end: return nums[start]
        left, right = start, end
        pivot = nums[(start + end) // 2]

        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left > right: break
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        #[start...right][?][left...end]
        if right - start + 1 >= k:
            return self.quickSelect(nums, start, right, k)
        elif left - start < k:
            return self.quickSelect(nums, left, end, k - left + start)
        return nums[right + 1]