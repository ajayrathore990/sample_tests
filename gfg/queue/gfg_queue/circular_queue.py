class Circular_List_Queue():
    def __init__(self,capacity):
        self.l = [None] * capacity
        self.capacity = capacity
        self.size = 0
        self.front = 0
        
    def is_empty(self):
        return self.size == 0
    
    def size(self):
        return self.size
    
    def get_front(self):
        if self.size ==0:
            return None
        else:
            return self.l[self.front]
    
    def get_rear(self):
        if self.size ==0:
            return None
        else:
            rear= (self.front+self.size-1) % self.capacity
            return self.l[rear]
    
    def enqueue(self,item):
        if self.size==self.capacity:
            return 
        else:
            rear = (self.front+self.size -1) % self.capacity
            rear = (rear +1) % self.capacity
            self.l[rear] = item
            self.size = self.size+1
    
    def dequeue(self):
        if self.size==0:
            return None
        else:
            res =self.l[self.front]
            self.front =( self.front +1) % self.capacity
            self.size=self.size-1
            return res 

