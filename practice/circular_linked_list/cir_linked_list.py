class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


class CircularLinkedList(object):
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        values = []
        values.append(node.value)
        while node.next != self.head:
            node = node.next
            values.append(node.value)
           
        return '-->'.join(values) 

    def insert(self, value):
        if self.head:
            node = self.head
            while node.next != self.head:
                node = node.next
            node.next = Node(value, None)
            node.next.next = self.head
       
            
        else:
            self.head = Node(value, None)
            self.head.next = self.head
           
  
    def delete(self):
       if self.head:
           
           node = self.head
           while node.next != self.head:
               node = node.next
           if self.head == node.next == self.head.next:
               self.head = None
           else:    
               self.head = self.head.next
               node.next = self.head

       else:
           raise Exception("Nothing to delete")
