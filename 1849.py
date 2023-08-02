###
同向双指针
滑动窗口，隔板法
###

class Solution:
    """
    @param customers: the number of customers
    @param grumpy: the owner's temper every day
    @param x: X days
    @return: calc the max satisfied customers
    """
    def max_satisfied(self, customers, grumpy, x):
        if not customers:
            return 0

        happy = 0
        max_happy = 0
        for customer_i, grumpy_i in zip(customers, grumpy):
            if grumpy_i == 0:
                happy += customer_i
        
        left = 0
        for right in range(len(customers)):
            if grumpy[right] == 1:
                happy += customers[right]
            
            if right - left + 1 > x:
                if grumpy[left] == 1:
                    happy -= customers[left]
                left += 1
            
            max_happy = max(max_happy, happy)
        return max_happy
        
