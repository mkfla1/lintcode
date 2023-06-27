class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """
    def subarray_sum_equals_k_i_i(self, nums: List[int], k: int) -> int:
        if not nums: return -1
        prefix_sum = self.get_prefix_sum(nums)
        sumToIndex = {0: 0}
        min_length = float('inf')

        for end in range(1, len(prefix_sum)):
            target = prefix_sum[end] - k
            if target in sumToIndex:
                min_length = min(min_length, end - sumToIndex[target])
            sumToIndex[prefix_sum[end]] = end
        return min_length if min_length != float('inf') else -1    

    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for val in nums:
            prefix_sum.append(prefix_sum[-1] + val)
        return prefix_sum  