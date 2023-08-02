###
同向双指针
###

from collections import defaultdict
class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def k_distinct_characters(self, s: str, k: int) -> int:
        letter_to_count = defaultdict(int)
        valid_count = 0
        slow = 0
        ans = 0

        for fast, letter in enumerate(s):
            letter_to_count[letter] += 1
            if letter_to_count[letter] == 1:
                valid_count += 1
            
            while slow <= fast and valid_count >= k:
                ans += len(s) - fast
                letter_to_count[s[slow]] -= 1
                if letter_to_count[s[slow]] == 0:
                    valid_count -= 1
                slow += 1
        return ans
