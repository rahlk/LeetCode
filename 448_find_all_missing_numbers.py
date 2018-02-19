"""
Given an array of integers where 1 <= a[i] <= n (n = size of array), some elements 
appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Note: Do it without extra space and in O(n) runtime. You may assume the returned
list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        Using set operations

        :type nums: List[int]
        :rtype: List[int]
        """
        
        "given = [4,3,2,7,8,3,1]"
        "full =  [1,2,3,4,5,6,7,8]"
        
        returned = set(range(1, len(nums)+1)) # Assume returned list contains all numbers
        returned = list(returned.difference(set(nums)))
        return returned

def _test():
    s = Solution()
    print s.findDisappearedNumbers(nums=[4, 3, 2, 7, 8, 2, 3, 1])

if __name__ == "__main__":
    _test()

