
class Stack:
    def __init__(self):
        self.stack =[]
        self.max = 4
    
    def is_empty(self):
        if len(self.stack) ==0:
            return True
        else:
            return False

    def insert(self, item):
        if len(self.stack) < self.max:
            self.stack.append(item)
            return self.stack
        else:
            return 0
    
    def pop(self):
        if len(self.stack)>self.max:
            return self.stack.pop()
        else:
            return 0

    def top_element(self):
        if self.is_empty():
            return 0
        else:
            return self.stack[0]

    def check_element(self,item):
        if item in self.stack:
            return True
        else:
            return False


s = Stack()        
obj =s.insert(22)
obj =s.insert(220)
obj =s.insert(221)
obj =s.insert(222)
obj =s.check_element(223)
print(obj)