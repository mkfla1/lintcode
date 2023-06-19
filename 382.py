###
相向双指针, twoSum型
O(n^2)
###

class Solution:
    """
    @param s: A list of integers
    @return: An integer
    """
    def triangle_count(self, s: List[int]) -> int:
        if len(s) <= 2: return 0
        edges = sorted(s)
        count = 0

        for cIndex in range(2, len(edges)):
            count += self.twoSum(edges, cIndex)
        return count
    
    def twoSum(self, edges, cIndex):
        left, right = 0, cIndex - 1
        count = 0

        while left < right:
            val = edges[left] + edges[right]

            if val > edges[cIndex]:
                count += right - left
                right -= 1
            else:
                left += 1
        return count
