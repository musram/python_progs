class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value



class Queue(object):
    def __init__(self):
        self.front = None
        self.rear = None


    def __repr__(self):
        node = self.front
        nodes = []
        while self.rear != self.front:
            nodes.append(node.value)
            node = node.next
        return '-->'.join(nodes)

    def enque(self, value):
        node = Node(value)
        if self.rear:
            self.rear.next  = node
            self.rear = node
        else:
            self.rear = self.front = node


    def deque(self):
        if self.rear == self.front != None:
            value = self.front.value
            self.rear = self.front = None
            return  value

        elif self.rear == self.front == None:
            return

        else:
            node = self.front
            self.front = node.next
            return node.value
            
            
            
