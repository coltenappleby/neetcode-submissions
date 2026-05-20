class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum == None:
            self.minimum = val
        else: 
            self.minimum = min(self.minimum, val) 

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minimum:
            if not self.stack:
                self.minimum = None
            else:
                self.minimum = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
