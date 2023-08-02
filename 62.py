###
二分法
###

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[-1]:
                if target <= nums[-1]:
                    start = mid
                elif nums[mid] > target:
                    end = mid
                else:
                    start = mid
            else:
                if target > nums[-1]:
                    end = mid
                elif nums[mid] < target:
                    start = mid
                else:
                    end = mid
        
        if nums[start] == target: return start
        if nums[end] == target: return end
        return -1


###
二分法
将上面重复的代码精简
O(logn)
###
class Solution:
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

