class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        s = [val, val]
        if len(self.stack) != 0:
            s[1] = min(self.stack[-1][1], val)
        self.stack.append(s)

    def pop(self) -> None:
        self.stack.pop(-1)
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())