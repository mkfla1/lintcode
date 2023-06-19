"""
对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。
"""



"""
最直接的思路
逐个匹配
O(n^2)
"""
class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str(self, source: str, target: str) -> int:
        if not target: return 0
        if not source: return -1

        found = False
        for i in range(len(source) - len(target) + 1):
            found = True
            for j in range(len(target)):
                if source[i + j] != target[j]: 
                    found = False
                    break
            if found: return i
        return -1


"""
Robin-Karp
把target转化成数字targetCode
匹配时每添加一个字符都能在O(1)时间内算出新的code, 并和targetCode比对
如果相同，doubleCheck俩个字符片段，相同就找到结果了
O(n)
"""
BASE = 1000000
SEED = 31

class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str(self, source: str, target: str) -> int:
        if not target: return 0
        if not source: return -1

        power, targetCode = self.setUp(target)
        code = 0

        for i in range(len(source)):
            self.append(code, source[i])

            if i < len(target) - 1: continue
            if i >= len(target):
                self.removeHead(code, source[i - len(target)], power)
            
            if code == targetCode:
                left = i - len(target) + 1
                if source[left: i + 1] == target:
                    return left
        return -1
    
    def append(self, code, letter):
        code = (code * SEED + ord(letter)) % BASE
        return code
    
    def removeHead(self, code, letter, power):
        code = code - ord(letter) * power
        if code < 0:
            code += BASE
        code %= BASE
        return code
    
    def setUp(self, target):
        power = 1
        code = 0
        
        for i in range(len(target)):
            self.append(code, target[i])
            power = power * SEED % BASE
        return (power, code)





