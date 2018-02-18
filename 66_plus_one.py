from pdb import set_trace


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = sum([d*10**i for i, d in enumerate(digits[::-1])])
        return [int(s) for s in str(number+1)]

if __name__ == "__main__":
    s = Solution()
    print s.plusOne([9,9])