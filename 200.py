"""
200 · 最长回文子串
"""


"""
方法一
枚举中轴线位置(left, right)，有重复得利用子函数；然后背向双指针， O(n^2)
"""

class Solution:
    def longest_palindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        result = (1, 0) #(length, startIndex)
        
        for i in range(len(s)):
            result = max(result, self.helper(s, i, i), self.helper(s, i, i + 1))
        
        return s[result[1]: result[1] + result[0]]
    
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        left += 1
        right -= 1
        return (right - left + 1, left)

"""
方法二
枚举长度和起始点(O^2)， 然后最关键的检测是否时回文，
由于有大量重复，我们利用区间型动态规划， 利用O(n^2)额外空间记录下所有isPalindrome即可，
这样后续只需要O(1)时间来查询, 那么总时间复杂度还是O(n^2)
"""
class Solution:
    def longest_palindrome(self, s: str) -> str:
        if not s: return ""
        isPalindrome = self.getIsPalindrome(s)

        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if isPalindrome[start][start + length - 1]:
                    return s[start: start + length]
    
    def getIsPalindrome(self, s):
        isPalindrome = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            isPalindrome[i][i] = True
        for i in range(len(s) - 1):
            isPalindrome[i][i + 1] = s[i] == s[i + 1]
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 2, len(s)):
                isPalindrome[i][j] = isPalindrome[i + 1][j - 1] and s[i] == s[j]
        return isPalindrome
