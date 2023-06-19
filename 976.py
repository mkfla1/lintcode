###
四数之和的follow up
思路不在使用双指针了
由于是求方案数，那意味着可以加速
这里采用折半处理的思想
先处理a,b数组+哈希表
然后处理c,d的组合
O(n^2)
###


class Solution:
    """
    @param a: a list
    @param b: a list
    @param c: a list
    @param d: a list
    @return: how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
    """
    def four_sum_count(self, a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
        valToCount = {}
        for aVal in a:
            for bVal in b:
                val = aVal + bVal
                valToCount[val] = valToCount.get(val, 0) + 1
        
        ans = 0
        for cVal in c:
            for dVal in d:
                target = -cVal - dVal
                ans += valToCount.get(target, 0)
        return ans
