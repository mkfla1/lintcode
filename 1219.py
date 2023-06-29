###
二分法
###
class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def find_radius(self, houses: List[int], heaters: List[int]) -> int:
        houses = sorted(houses)
        heaters = sorted(heaters)
        ans = float('-inf')

        for house in houses:
            distance = self.get_distance(heaters, house)
            ans = max(ans, distance)
        return ans
    
    def get_distance(self, heaters, house):
        start, end = 0, len(heaters) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if heaters[mid] == house:
                return 0
            if heaters[mid] < house:
                start = mid
            else:
                end = mid
        
        distance = min(abs(heaters[start] - house), abs(heaters[end] - house))
        return distance


###
双数组同向双指针
###
class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def find_radius(self, houses: List[int], heaters: List[int]) -> int:
        houses = sorted(houses)
        heaters = sorted(heaters)
        distance = 0

        heater_index = 0
        for house in houses:
            while heater_index < len(heaters) - 1 and heaters[heater_index] < house:
                heater_index += 1
            
            curt = abs(house - heaters[heater_index])
            if heater_index - 1 >= 0:
                curt = min(curt, abs(house - heaters[heater_index - 1]))
            distance = max(distance, curt)
        return distance 

