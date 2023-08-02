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
        if not nums: return -1
        prefix_sum = [0]
        for val in nums:
            prefix_sum.append(prefix_sum[-1] + val)

        val_to_recent_index = {0: 0}
        min_length = float('inf')
        for i in range(1, len(prefix_sum)):
            target = prefix_sum[i] - k
            if target in val_to_recent_index:
                min_length = min(min_length, i - val_to_recent_index[target])
            val_to_recent_index[prefix_sum[i]] = i
        
        return min_length if min_length != float('inf') else -1

        
        
        
