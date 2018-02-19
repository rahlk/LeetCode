class Solution(object):
    def isPowerOfThree(self, n):
        """
        My recursive solution
        
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 3 == 0:
            return self.isPowerOfThree(n / 3)
        else:
            return False

    def isPowerOfThree_non_recr(self, n):
        """
        A non-recursive solution
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False

        while n % 3 == 0:
            n /= 3

        return n == 1


if __name__ == "__main__":
    s = Solution()
    print s.isPowerOfThree_non_recr(0)
