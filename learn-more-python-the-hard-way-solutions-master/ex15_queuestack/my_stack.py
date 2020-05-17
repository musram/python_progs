class StackNode:

    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __repr__(self):
        nval = self.value and  self.next or None 
        return '[{}:{}]'.format(self.value, nval)

class Stack:

    def __init__(self):
        self.top = None
        
    def push(self, value):
        self.top = StackNode(value, self.top)
        

    def count(self):
        counter = 0
        node = self.top
        while node:
            node = node.next
            counter += 1
        return counter

    def pop(self):
        if self.top == None:
            return
        else:
            node = self.top
            self.top = node.next
            return node.value

    def first(self):
        return self.top.value

            

    
            
        
