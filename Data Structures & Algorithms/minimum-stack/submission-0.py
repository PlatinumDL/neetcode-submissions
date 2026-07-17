class MinStack:

    def __init__(self):
        self.items = []   

    def push(self, val: int) -> None:
        #if stack is empty, set min to cur val
        if len(self.items) == 0:
            self.items.append((val,val))
        else:
            curMin = self.getMin()
            if val < curMin:
                self.items.append((val,val))
            else:
                self.items.append((val,curMin))

    def pop(self) -> None:
        #Just pop
        self.items.pop()

    def top(self) -> int:
        #Return last value
        if len(self.items) > 0:
            top, minimum = self.items[-1]
            return top

    def getMin(self) -> int:
        if len(self.items) > 0:
            top, minimum = self.items[-1]
            return minimum
        else:
            return 0
        
