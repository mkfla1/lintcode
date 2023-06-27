###
前缀和
###

class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def max_sub_array_len(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        prefix_sum = self.get_prefix_sum(nums)
        sum_to_index = {0: 0}
        max_length = 0

        for i in range(1, len(prefix_sum)):
            target = prefix_sum[i] - k
            if target in sum_to_index:
                max_length = max(max_length, i - sum_to_index[target])
            if prefix_sum[i] not in sum_to_index:
                sum_to_index[prefix_sum[i]] = i

        return max_length
    
    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for val in nums:
            prefix_sum.append(prefix_sum[-1] + val)
        return prefix_sum