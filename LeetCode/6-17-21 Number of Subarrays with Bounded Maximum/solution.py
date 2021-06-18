class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        consecutive_below_right = 0
        below_min_counter = 0
        total = 0

        for num in nums:
            if num < left:
                below_min_counter += 1
                consecutive_below_right += 1
            elif num > right:
                # add to total and clear
                if below_min_counter:
                    total -= consecutive_sum(below_min_counter)
                total += consecutive_sum(consecutive_below_right)
                consecutive_below_right = 0
                below_min_counter = 0
            else:
                consecutive_below_right += 1
                if below_min_counter:
                    total -= consecutive_sum(below_min_counter)
                    below_min_counter = 0

        return int(total + consecutive_sum(consecutive_below_right) - consecutive_sum(below_min_counter))

def consecutive_sum(n):
    '''Returns consecutive sum of 1 + 2 + ... + n.'''
    return (n / 2) * (n + 1)
