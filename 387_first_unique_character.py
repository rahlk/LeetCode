"""
Given a string, find the first non-repeating character in it and return it's 
index. If it doesn't exist, return -1.

Example:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
"""

from pdb import set_trace

class Solution(object):
    def firstUniqChar(self, s):
        """
        A simple solution. O(n^2). Slow for long strings
        :type s: str
        :rtype: int
        """
        
        for i, char in enumerate(s):
            if char not in s[:i] + s[i + 1:]:
                return i

        return -1

    def leetcode_elegant_firstUniqChar(self, s):
        """
        An elegant solution from LeetCode discussion boards.
        Still doesn't work on very long strings.

        :type s: str
        :rtype: int
        """
        index = []
        for char in set(s):
            if s.count(char) == 1:
                index.append(s.index(char))
        return min(index) if len(index) > 0 else -1

    def fast_firstUniqChar(self, s):
        """
        A fast solution that uses dictionaries. Solves in O(n) time. O(n) space.

        :type s: str
        :rtype: int
        """
        index = {a.lower():s.count(a) for a in set(s)}
        
        if 1 in index.values():
            for char in s:
                if index[char.lower()] == 1:
                    return s.index(char)
        else:
            return -1
            



def _test():
    s = Solution()
    f = open("long_string.txt")
    print s.fast_firstUniqChar(s="")
    # print s.fast_firstUniqChar(s=f.read())

if __name__ == "__main__":
    _test()
