class StackNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value


class Stack(object):
    def __init__(self):
        self.top = None
        self._count = 0

    def __repr__(self):
        node = self.top
        nodes = []
        while node:
            nodes.append(node.value)
            node = node.next

        return '-->'.join(nodes)

    def push(self, value):
        node = StackNode(value)
        if self.top:
            node.next = self.top
            self.top = node

        else:
            self.top = node
        self._count += 1    
            
    def pop(self):
        if self.top:
           node = self.top
           self.top = node.next
           self._count -= 1 
           return node.value

        else:
           return

    def count(self):
        return self._count
