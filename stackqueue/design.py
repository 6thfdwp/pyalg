class MinStack:
    """
    https://www.interviewbit.com/problems/min-stack/
    push, pop, top (peek) and getMin all O(1)
    
    Keep a single min value to update every time new el is pushed, it is not enough
    as need to loop current stack to check new min when popping
    We can also store (val, curMin) in every el, but this would get lots of redundancy
    when push in ascending order 1,5,6,7

    Or Use extra list to only store min el when there is new min gets pushed
    remember to pop two list when the current min gets popped

    Clarify:
    pop: should return popped value?
    top and getMin: what to return when empty
    """
    def __init__(self):
        self._stack = []
        self._top = -1

    def __str__(self):
        return ','.join([ str(el[0]) for el in self._stack ])

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

class QStack(object):
    """
    docstring for ClassName
    """
    def __init__(self, arg):
        self.arg = arg


if __name__ == '__main__':
    ms = MinStack()
    ms.push(5)
    ms.push(1)
    print ms
    print ms.getMin()
    print ms.pop()
    print ms



