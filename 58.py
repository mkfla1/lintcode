###
最终转化成两数之和
O(n^3)
###

class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
             we will sort your return value in output
    """
    def four_sum(self, numbers: List[int], target: int) -> List[List[int]]:
        if not numbers or len(numbers) <= 3: return []
        numbers = sorted(numbers)
        ans = []

        for aIndex in range(len(numbers)):
            if aIndex > 0 and numbers[aIndex] == numbers[aIndex - 1]: 
                continue
            for bIndex in range(aIndex + 1, len(numbers)):
                if bIndex > aIndex + 1 and numbers[bIndex] == numbers[bIndex - 1]:
                    continue
                self.twoSum(numbers, aIndex, bIndex, target, ans)
        return ans
    
    def twoSum(self, numbers, aIndex, bIndex, target, ans):
        left, right = bIndex + 1, len(numbers) - 1
        target = target - numbers[aIndex] - numbers[bIndex]
        previous = None

        while left < right:
            val = numbers[left] + numbers[right]
            if val == target:
                if (numbers[left], numbers[right]) != previous:
                    ans.append([numbers[aIndex], numbers[bIndex], numbers[left], numbers[right]])
                previous = (numbers[left], numbers[right])
                left += 1
                right -= 1
            elif val < target:
                left += 1
            else:
                right -= 1

