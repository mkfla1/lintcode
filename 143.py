###
O(nlogk)
推测时间复杂度在计数下O(n)～快排下O(nlogn)之间得出O(nlogk)
可能是n次循环或者logk次循环，本题是是采取的后者，
分治颜色 + partition数组，分治判断轴是midColor = (colorStart + colorEnd) // 2, 那么共logk次循环 
###
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sort_colors2(self, colors: List[int], k: int):
        if not colors: return
        self.partition(colors, 0, len(colors) - 1, 1, k)
    
    def partition(self, colors, start, end, startColor, endColor):
        if start >= end or startColor >= endColor: return
        left, right = start, end
        pivot = (startColor + endColor) // 2

        while left <= right:
            while left <= right and colors[left] <= pivot:
                left += 1
            while left <= right and colors[right] > pivot:
                right -= 1
            if left > right: break
            colors[left], colors[right] = colors[right], colors[left]
            left += 1
            right -= 1
        
        #start...right?left...end
        self.partition(colors, start, right, startColor, pivot)
        self.partition(colors, left, end, pivot + 1, endColor)
