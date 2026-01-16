from collections import deque

class Deque_queue():
    def __init__(self):
        self.queue= deque()

    def is_empty(self):
        if len(self.queue)==0:
            return True
        else:
            return False
    
    def insert(self,item):
        self.queue.append(item)
        return item
        
    def remove(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return 0
       
obj  = Deque_queue()
obj.insert(1)
obj.remove()
print(obj.is_empty())
