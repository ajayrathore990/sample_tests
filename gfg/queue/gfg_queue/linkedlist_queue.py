class Node():
    def __init__(self,key):
        self.key = key
        self.next = None

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
    def is_empty(self):
        return self.size == 0
    
    def size(self):
        return self.size
    
    def get_front(self):
        return self.front.key
    
    def get_rear(self):
        return self.rear.key
    
    def enqueue(self,item):
        temp =Node(item)
        if self.rear ==None:
            self.front =temp
        else:
            self.rear.next= temp
        self.rear =temp
        self.size = self.size +1
        
    def dequeue(self):
        if self.front ==None:
            return 0
        else:
            res = self.front.key
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            self.size = self.size -1 
            return res 


