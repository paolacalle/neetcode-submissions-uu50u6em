class MinStack:

    def __init__(self):
        self.stack = []
        self.pre = []
        

    def push(self, val: int) -> None:
        if self.pre and self.pre[-1] < val:
            self.pre.append(self.pre[-1])
        else:
            self.pre.append(val) 

        self.stack.append(val)

        # print(f"s: {self.stack} ... pre: {self.pre}")
        return None

    def pop(self) -> None:
        self.stack.pop()
        self.pre.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.pre[-1]
        
