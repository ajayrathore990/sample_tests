from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def insert(self,item):
            self.stack.append(item)
            return self.stack
        
    def delete(self):
        if self.stack:
            self.stack.pop()
        else:
            return 0
    
    def show(self):
        return list(self.stack)
