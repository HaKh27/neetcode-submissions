class MinStack:

    def __init__(self):
        self.stack=[]
        self.small=[]
        

    def push(self, val: int) -> None:
        if not self.small: 
            self.small.append(val) 
        elif val<self.small[-1]: 
            self.small.append(val) 
        else:
            self.small.append(self.small[-1])
   
        self.stack.append(val)
        

    def pop(self) -> None:
        del self.stack[-1]
        del self.small[-1]
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.small[-1]
        
