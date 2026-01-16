class List_queue():
    def __init__(self):
        self.queue = []

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
            return self.queue.pop(0)
        else:
            return 0
        
    def get_front(self):
        return self.queue[0]
    
    def get_rear(self):
        return self.queue[-1]
    
