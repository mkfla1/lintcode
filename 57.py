###
O(n^2)
去重的基本操作：只用第一个代表
###
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """
    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        if len(numbers) < 3: return []
        numbers = sorted(numbers)
        ans = []

        for aIndex in range(len(numbers)):
            if aIndex > 0 and numbers[aIndex] == numbers[aIndex - 1]:
                continue
            self.twoSum(numbers, aIndex, ans)
        return ans
    
    def twoSum(self, numbers, aIndex, ans):
        target = -numbers[aIndex]
        left, right = aIndex + 1, len(numbers) - 1
        previous = None

        while left < right:
            curt = numbers[left] + numbers[right]
            if curt == target:
                if (numbers[left], numbers[right]) != previous:
                    ans.append([numbers[aIndex], numbers[left], numbers[right]])
                previous = (numbers[left], numbers[right])
                left += 1
                right -= 1
            elif curt < target:
                left += 1
            else:
                right -=1



