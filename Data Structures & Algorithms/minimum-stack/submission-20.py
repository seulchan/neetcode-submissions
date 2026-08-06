class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_val = min(val, self.min_val) if self.min_val != None else val
        self.min_stack.append(self.min_val)        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        self.min_val = self.min_stack[-1] if self.min_stack else None

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        print(self.min_stack)
        return self.min_stack[-1]
        
