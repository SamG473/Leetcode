class MinStack:

    def __init__(self):
        self.stack = [] 
        self.mins = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.mins:
            self.mins.append(value)                    
        else:
            self.mins.append(min(value, self.mins[-1]))  
        

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
