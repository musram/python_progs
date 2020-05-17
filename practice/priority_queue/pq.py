class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = next

    def __repr__(self):
        return '{}={}'.format(self.key, self.value)

class PQ(object):
    def __init__(self):
        self.front = None

    def __repr__(self):
        node = self.front
        nodes = []
        while node:
            nodes.append(node.value)
            node = node.next
        return '-->'.join(nodes)

    def insert(self, key, value):
        if self.front:
            node = self.front
            prev = self.front
            while node.next:
                prev = node
                node = node.next
                if key > node.key:
                    
          
            prev.next = Node(key, value)
            prev.next.next = node
            node = Node(key, value)
            node.next = self.front
            self.front = node
        else:
            self.front = Node(key, value)

    def delete(self):
        if self.front:
            node = self.front
            prev = self.front        
            while node.next:
                node = node.next
                prev = node    
            prev.next = None        
        else:
            raise Exception("PQ empty")
            