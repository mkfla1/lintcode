###
隔板法+滑动窗口
###
class Solution:
    """
    @param a: a list of integer
    @param k: a integer
    @param l: a integer
    @return: return the maximum number of apples that they can collect.
    """
    def pick_apples(self, apples: List[int], k: int, l: int) -> int:
        max_apple = -1

        for i in range(k - 1, len(apples) - l):
            left_apple = self.get_apple(apples, k, 0, i)
            right_apple = self.get_apple(apples, l, i + 1, len(apples) - 1)
            max_apple = max(max_apple, left_apple + right_apple)
        
        for i in range(l - 1, len(apples) - k):
            left_apple = self.get_apple(apples, l, 0, i)
            right_apple = self.get_apple(apples, k, i + 1, len(apples) - 1)
            max_apple = max(max_apple, left_apple + right_apple)
        return max_apple
    
    def get_apple(self, apples, tree, start, end):
        max_apple = 0
        left = start
        curt = 0

        for right in range(start, end + 1):
            curt += apples[right]
            if right - left + 1 > tree:
                curt -= apples[left]
                left += 1
            max_apple = max(max_apple, curt)
        return max_apple
