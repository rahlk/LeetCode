"""
Given an array of integers, 1 <= a[i] <= n (n = size of array), some elements 
appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

from collections import Counter


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = Counter(nums)
        return [key for key in counts.keys() if counts[key]==2]

def _test():
    from random import randint
    s = Solution()
    print s.findDuplicates(nums=[randint(0,100) for _ in xrange(100)])

if __name__ == "__main__":
    _test()