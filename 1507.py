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
class SegmentTree:
    class TreeNode:
        def __init__(self, start, end, val):
            self.start, self.end = start, end
            self.left, self.right = None, None
            self.val = val

    def __init__(self, start, end):
        self.root = self.build(start, end)

    def build(self, start, end):
        if start == end:
            return SegmentTree.TreeNode(start, end, float('-inf'))
        
        root = SegmentTree.TreeNode(start, end, float('-inf'))
        mid = (start + end) // 2
        root.left = self.build(start, mid)
        root.right = self.build(mid + 1, end)
        return root
    
    def update_node_val(self, root):
        root.val = float('-inf')
        if root.left:
            root.val = max(root.val, root.left.val)
        if root.right:
            root.val = max(root.val, root.right.val)
    
    def query(self, root, start, end):
        if root.start == start and root.end == end:
            return root.val
        
        mid = (root.start + root.end) // 2
        if mid < start:
            return self.query(root.right, start, end)
        elif mid >= end:
            return self.query(root.left, start, end)
        return max(self.query(root.left, start, mid), self.query(root.right, mid + 1, end))
    
    def update(self, root, index, val):
        if root.start == index and root.end == index:
            root.val = val
            return
        
        mid = (root.start + root.end) // 2
        if mid < index:
            self.update(root.right, index, val)
        else:
            self.update(root.left, index, val)
        self.update_node_val(root)
        return      

class Solution:
    def shortest_subarray(self, nums: List[int], k: int) -> int:
        prefix_sum = self.get_prefix_sum(nums)
        sum_to_index = self.get_discrete_sum_to_index(prefix_sum, k)
        st = SegmentTree(0, len(sum_to_index) - 1)
        min_length = float('inf')

        for end, sum in enumerate(prefix_sum):
            st.update(st.root, sum_to_index[sum], end)
            start = st.query(st.root, st.root.start, sum_to_index[sum - k])
            if start != float('-inf'):
                min_length = min(min_length, end - start)
        
        return min_length if min_length != float('inf') else -1
    
    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for val in nums:
            prefix_sum.append(prefix_sum[-1] + val)
        return prefix_sum
    
    def get_discrete_sum_to_index(self, nums, k):
        nums_set = set()
        for val in nums:
            nums_set.add(val)
            nums_set.add(val - k)
        
        sum_to_index = {}
        for i, val in enumerate(sorted(list(nums_set))):
            sum_to_index[val] = i
        return sum_to_index   

