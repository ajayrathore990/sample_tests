class Stack:
    def __init__(self):
        self.stack=[]

    def insert(self,item):
            self.stack.append(item)
            return self.stack
    
    def show(self):
        return self.stack


