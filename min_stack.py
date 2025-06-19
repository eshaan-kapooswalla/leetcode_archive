# Solution for LeetCode problem: Min Stack

def solution():
    """
    Implements a Min Stack. Example usage:
    stack = MinStack()
    stack.push(val)
    stack.pop()
    top = stack.top()
    min_val = stack.getMin()
    """
    class MinStack:
        def __init__(self):
            self.stack = []
            self.min_stack = []
        def push(self, val: int) -> None:
            self.stack.append(val)
            if not self.min_stack or val <= self.min_stack[-1]:
                self.min_stack.append(val)
        def pop(self) -> None:
            if self.stack:
                val = self.stack.pop()
                if val == self.min_stack[-1]:
                    self.min_stack.pop()
        def top(self) -> int:
            if not self.stack:
                raise IndexError("Stack is empty")
            return self.stack[-1]
        def getMin(self) -> int:
            if not self.min_stack:
                raise IndexError("Min stack is empty")
            return self.min_stack[-1]
    # Example usage:
    # stack = MinStack()
    # stack.push(-2)
    # stack.push(0)
    # stack.push(-3)
    # print(stack.getMin()) # returns -3
    # stack.pop()
    # print(stack.top())    # returns 0
    # print(stack.getMin()) # returns -2
    pass
