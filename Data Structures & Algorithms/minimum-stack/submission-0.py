class MinStack:

    def __init__(self):
        self.stack = []
        self.myMin = float('inf')
    def push(self, val: int) -> None:
        self.stack.append((val, self.myMin))
        if val < self.myMin:
            self.myMin = val
    def pop(self) -> None:
        if self.stack:
            self.myMin = self.stack[-1][1]
            self.stack.pop()
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
    def getMin(self) -> int:
        return self.myMin
