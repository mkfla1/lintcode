###
同向双指针 + 哈希表defaultdict
###

from collections import defaultdict

class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def min_window(self, source: str, target: str) -> str:
        if not target: return ""
        if not source: return ""

        targert_to_count = defaultdict(int)
        for letter in target:
            targert_to_count[letter] += 1
        
        slow = 0
        valid_count = 0
        length, start = float('inf'), -1
        for fast, letter in enumerate(source):
            if letter not in targert_to_count: continue
            targert_to_count[letter] -= 1
            if targert_to_count[letter] == 0:
                valid_count += 1
            
            while slow <= fast and valid_count == len(targert_to_count):
                if (new_length := fast - slow + 1) <= length:
                    length, start = new_length, slow
                if source[slow] not in targert_to_count:
                    slow += 1
                    continue

                if targert_to_count[source[slow]] == 0:
                    valid_count -= 1
                targert_to_count[source[slow]] += 1
                slow += 1

        if length == float('inf'):
            return ""
        return source[start: start + length]

                

