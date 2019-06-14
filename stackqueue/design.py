class MinStack:
    """
    push, pop, top (peek) and getMin all O(1)
    
    Keep a single min value to update every time new el is pushed, it is not enough
    as need to loop current stack to find new min when popping

    Clarify:
    """
    def __init__(self):
        self._stack = []
        self._top = -1

    def isEmpty(self):
        return self._top == -1

    # @param x, an integer
    def push(self, x):
        curMin = self.getMin()
        curMin = x if self.isEmpty() else min(x, curMin)

        self._top += 1
        self._stack.append((x, curMin))

    # @return nothing
    def pop(self):
        if self.isEmpty():
          return
        self._top -= 1
        self._stack.pop()


    # @return an integer
    def top(self):
        if self.isEmpty():
          return -1
        return self._stack[self._top][0]


    # @return an integer
    def getMin(self):
        if self.isEmpty():
          return -1

        return self._stack[self._top][1]
