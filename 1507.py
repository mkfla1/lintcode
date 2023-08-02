###
前缀和暴力法
O(n^2)
###

class Solution:
    """
    @param a: the array
    @param k: sum
    @return: the length
    """
    def shortest_subarray(self, nums: List[int], k: int) -> int:
        if not nums: return -1
        prefix_sum = self.get_prefix_sum(nums)
        min_length = float('inf')

        for right in range(1, len(prefix_sum)):
            for left in range(0, right):
                if prefix_sum[right] - prefix_sum[left] >= k:
                    min_length = min(min_length, right - left)
        return min_length if min_length != float('inf') else -1
    
    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for val in nums:
            prefix_sum.append(prefix_sum[-1] + val)
        return prefix_sum


###
logn次O(n)的操作
二分答案+能够O(1)删除的自定义堆+前缀和
O(n(logn)^2)
###
from heapq import heappush, heappop

class Heap:
    def __init__(self):
        self.minHeap = []
        self.deleted_index = set()
    
    def push(self, val, index):
        heappush(self.minHeap, (val, index))
    
    def _lazy_delete(self):
        while self.minHeap and self.minHeap[0][1] in self.deleted_index:
            self.deleted_index.remove(self.minHeap[0][1])
            heappop(self.minHeap)
    
    def delete_by_index(self, index):
        self.deleted_index.add(index)
    
    def top(self):
        self._lazy_delete()
        return self.minHeap[0]

class Solution:
    """
    @param nums: the array
    @param k: sum
    @return: the length
    """
    def shortest_subarray(self, nums: List[int], k: int) -> int:
        if not nums: return -1
        prefix_sum = self.get_prefix_sum(nums)

        start, end = 1, len(nums)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.check_valid(prefix_sum, mid, k):
                end = mid
            else:
                start = mid
        
        if self.check_valid(prefix_sum, start, k):
            return start
        if self.check_valid(prefix_sum, end, k):
            return end
        return -1
    
    def check_valid(self, prefix_sum, length, k):
        heap = Heap()
        heap.push(0, 0)

        for right in range(1, len(prefix_sum)):
            if right > length:
                heap.delete_by_index(right - length - 1)
            heap.push(prefix_sum[right], right)
            curt_sum = prefix_sum[right] - heap.top()[0]
            if curt_sum >= k:
                return True
        return False
    
    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for val in nums:
            prefix_sum.append(prefix_sum[-1] + val)
        return prefix_sum           
        
###
线段树
O(nlogn)
###
from typing import (
    List,
)
class SegmentTree:
    class TreeNode:
        def __init__(self, start, end, val):
            self.start, self.end = start, end
            self.left, self.right = None, None
            self.val = val
    
    def __init__(self, length):
        self.root = self.build(0, length - 1)
    
    def build(self, start, end):
        if start > end: return None
        root = self.TreeNode(start, end, -1)
        if start == end: return root

        mid = (start + end) // 2
        root.left = self.build(start, mid)
        root.right = self.build(mid + 1, end)
        return root
    
    def query(self, start, end, root=None):
        if root is None:
            root = self.root
        if root.start >= start and root.end <= end:
            return root.val
        if root.start > end or root.end < start:
            return -1
        return max(self.query(start, end, root.left), self.query(start, end, root.right))
    
    def update(self, index, val, root=None):
        if root is None: root = self.root

        if root.start == root.end:
            root.val = val
            return
        
        mid = (root.start + root.end) // 2
        if mid < index:
            self.update(index, val, root.right)
        else:
            self.update(index, val, root.left)
        root.val = max(root.left.val, root.right.val)
        
class Solution:
    """
    @param a: the array
    @param k: sum
    @return: the length
    """
    def shortest_subarray(self, nums: List[int], k: int) -> int:
        if not nums: return -1

        prefix_sum, discrete_val_to_index = self.get_info(nums, k)
        st = SegmentTree(len(discrete_val_to_index))
        min_length = float('inf')
        st.update(discrete_val_to_index[0], 0)

        for i in range(1, len(prefix_sum)):
            curt_sum = prefix_sum[i]
            target_index = st.query(0, discrete_val_to_index[curt_sum - k])
            if target_index != -1 and i > target_index:
                min_length = min(min_length, i - target_index)
            st.update(discrete_val_to_index[curt_sum], i)
        return min_length if min_length != float('inf') else -1
    
    def get_info(self, nums, k):
        prefix_sum = [0]
        discrete_val_set = set([0])
        for val in nums:
            curt = val + prefix_sum[-1]
            prefix_sum.append(curt)
            discrete_val_set.add(curt)
            discrete_val_set.add(curt - k)
        
        discrete_val_to_index = {val: i for i, val in enumerate(sorted(list(discrete_val_set)))}
        return (prefix_sum, discrete_val_to_index)




        

