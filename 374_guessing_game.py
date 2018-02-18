"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results 
(-1, 1, or 0)
"""
from pdb import set_trace

def guess(num):
    actual = 6
    if num < actual:
        return -1
    elif num > actual:
        return 1
    else:
        return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        def guessing(start, stop):
            if guess(start + (stop - start) / 2) < 0:
                return guessing(start + (stop - start) / 2, stop)

            elif guess(start + (stop - start) / 2) > 0:
                return guessing(start, start + (stop - start) / 2)

            else:
                return start + (stop - start) / 2

        return guessing(1, n)

if __name__ == "__main__":
    s = Solution()
    print s.guessNumber(100)
