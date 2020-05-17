class QueueNode(object):

    def __init__(self, value, nxt, prv):
        self.value = value
        self.next = nxt
        self.prev = prv

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return '[{}:next={}:prev={}]'.format(self.value, repr(nval), repr(pval))

class Queue(object):

    def __init__(self):
        self.tail = None
        self.head = None

    def shift(self, value):
        if self.head:
            node =  QueueNode(value, None, None)
            self.tail.next = node
            self.tail = node
        else:
            self.head = QueueNode(value, None, None)
            self.tail = self.head

    def unshift(self):

        if self.head:
            node = self.head
            if self.head == self.tail:
                node = self.head
                self.head = self.tail = None
            else:
                self.head = node.next
                self.head.prev = None
            return node.value

    def  drop(self):
        print(self.tail)
        if self.head:
           if self.head == self.tail:
               self.head = self.tail = None
           else:
               self.tail = self.tail.prev
               self.tail.next = None
        print(self.tail)     
            
        
    def first(self):
        return self.head != None and self.head.value or None

    def empty(self):
        return self.head  == None
       
    def count(self):
        counter = 0
        node = self.head
        while node:
           node = node.next
           counter += 1
           
        return counter
