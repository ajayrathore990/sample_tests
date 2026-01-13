import math

class Node():
    def __init__(self,item):
        self.data = item
        self.next =None
        
class Stack():
    def __init__(self):
        self.head= None
        self.size = 0
        
    def push(self,x):
        temp = Node(x)
        temp.next= self.head
        self.head = temp
        self.size = self.size + 1
        return x
    
    def size(self):
        return self.size
    
    def peek(self):
        if self.head == None:
            return math.inf
        return self.head.data
    
    def pop(self):
        if self.head == None:
            return math.inf
        res = self.head.data
        self.head = self.head.next
        self.size=self.size -1
        return res 


