"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Example 3:
Given s = "race car", return "race car"

Note:
The vowels does not include the letter "y".
"""

from pdb import set_trace


class Solution(object):
    def reverseVowels_regular(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a", "e", "i", "o", "u"]
        reversed_s = s[::-1]
        reversed = ""
        for i, char_i in enumerate(s):
            if char_i.lower() in vowels:
                for j, char_j in enumerate(reversed_s):
                    if char_j.lower() in vowels:
                        reversed += char_j
                        reversed_s = reversed_s[j+1:]
                        break

            else:
                reversed+=char_i
        
        return reversed
    
    def reverseVowels_regex(self, s):
        """
        A RegEx way of reversing only the vowels in the string

        :param s: Input string
        :type s: str
        :return: str
        """

        import re
        reversed_vowels = [char for char in s if char.lower() in "aeiou"]
        return re.sub("(?i)[aeiou]", lambda x: reversed_vowels.pop(), s)

if __name__ == "__main__":
    s = Solution()
    print s.reverseVowels_regex("aA")
