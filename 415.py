"""
相向双指针
"""

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def is_palindrome(self, s: str) -> bool:
        if len(s) <= 1: return True
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left >= right: break
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True