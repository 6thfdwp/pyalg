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
    https://leetcode.com/problems/implement-stack-using-queues/
    Only two (or one) queues, standard ops: enqueue, peek/dequeue to simulate stack order
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._que1 = []
    
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self._que1.append(x)
        l = self._que1.length - 1
        while l > 0:
          self._que1[l-1], self._que1[l] = self._que1[l], self._que1[l-1]
          l -= 1
          
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
          return False
        
        return self._que1.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
          return False
        return self._que1[0]
      
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self._que1) <= 0  

if __name__ == '__main__':
    ms = MinStack()
    ms.push(5)
    ms.push(1)




