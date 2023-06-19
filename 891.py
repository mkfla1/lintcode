"""
相向双指针
重复部分利用子函数
"""

class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def valid_palindrome(self, s: str) -> bool:
        if len(s) <= 1: return True

        left, right = self.getFirstDiff(s, 0, len(s) - 1)
        if left >= right: return True
        left1, right1 = self.getFirstDiff(s, left + 1, right)
        left2, right2 = self.getFirstDiff(s, left, right - 1)
        return left1 >= right1 or left2 >= right2
    
    def getFirstDiff(self, s, start, end):
        left, right = start, end
        while left <= right:
            if s[left] != s[right]: break
            left += 1
            right -= 1
        return (left, right)

