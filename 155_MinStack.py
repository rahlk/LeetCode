class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack) == 0:
            self.stack.append(x)
            self.max = x
        elif x < self.max:
            self.stack.append(x)
        else:
            mod = 2 *  x - self.max
            self.stack.append(mod)
            self.max = x

    def pop(self):
        """
        :rtype: void
        """
        if self.max <= self.stack[-1]:
            self.max = 2 *  self.Max - self.stack[-1]

        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """

        if self.max <= self.stack[-1]:
            return self.max
        else:
            return self.stack[-1]

    def getmax(self):
        """
        :rtype: int
        """
        return self.max



# Your MaxStack object will be instantiated and called as such:
maxStack = MaxStack()
print maxStack.push(3)
print maxStack.push(1)
print maxStack.push(5)
print maxStack.push(0)
print maxStack.getmax()
print maxStack.pop()
print maxStack.top()
print maxStack.getmax()
print maxStack.getmax()
