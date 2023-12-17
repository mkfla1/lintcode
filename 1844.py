###
借助哈希表加速
遍历前缀和数组，同时使用一个字典sumToIndex记录每个前缀和对应的索引位置。对于每个前缀和，计算目标值target，即prefix_sum[end] - k，如果target存在于sumToIndex字典中，表示找到了和为k的子数组。
###

class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """
    def subarray_sum_equals_k_i_i(self, nums: List[int], k: int) -> int:
        # write your code here
        if not nums: return -1
        sum_to_last_index = {0: 0}
        prefix_sum = 0
        min_length = float('inf')

        for end in range(1, len(nums) + 1):
            prefix_sum += nums[end - 1]
            if (target := prefix_sum - k) in sum_to_last_index:
                min_length = min(min_length, end - sum_to_last_index[target])
            sum_to_last_index[prefix_sum] = end
        return min_length if min_length != float('inf') else -1             
