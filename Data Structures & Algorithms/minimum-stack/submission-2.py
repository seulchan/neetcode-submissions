class MinStack:

    def __init__(self):
        self.min_val = None
        self.stack = []

    def push(self, val: int) -> None:
        if self.min_val == None:
            self.min_val = val
        elif self.min_val > val:
            self.min_val = val
        self.stack.append((val, self.min_val))
        
    def pop(self) -> None:
        temp = self.stack.pop()[1]
        if temp == self.min_val:
            if len(self.stack) != 0:
                self.min_val = self.stack[-1][1]
            else:
                self.min_val = None

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
