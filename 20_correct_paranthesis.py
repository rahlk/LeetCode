class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 == 1:
            return False
        else:
            stack=[None]
            pairs = {
                "]": "[",
                "}": "{",
                ")": "("
            }
            for char in s:
                if char in pairs.values():
                    stack.append(char)
                if char in pairs.keys() and pairs[char] != stack.pop():
                    return False
        
        return len(stack) >= 1


if __name__ == "__main__":
    random_string = "]["
    s = Solution()
    print s.isValid(random_string)
