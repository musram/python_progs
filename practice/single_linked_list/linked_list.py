class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value


class LinkedList(object):
    def __init__(self):
        self.begin = None

    def __repr__(self):
        node = self.begin
        values = []
        while node:
            values.append(node.value)
            node = node.next
        return '-->'.join(values)

    def add_last(self, value):
       
        if self.begin:
            node = self.begin
            while node.next:
                node = node.next
            node.next = LinkedListNode(value)
        else:
            self.begin = LinkedListNode(value)
            

    def add_first(self, value):
        node = LinkedListNode(value)
        node.next = self.begin
        self.begin = node


    def add_after(self, target_node_data, value):
        if self.begin:
            node = self.begin
            while node:
                
                if node.value == target_node_data:
                    insert_node = LinkedListNode(value)
                    insert_node.next  = node.next
                    node.next = insert_node
                    return
                node = node.next
                
            raise Exception("Node with data '%s' not found" % target_node_data)
        else:
            raise Exception("List empty")
            
    def add_before(self, target_node_data, value):
        if self.begin:
            node = self.begin
            prev = self.begin
            while node:
                
                if node.value == target_node_data:
                    insert_node = LinkedListNode(value)
                    insert_node.next  = node
                    prev.next = insert_node
                    return
                prev = node
                node = node.next
                
                
            raise Exception("Node with data '%s' not found" % target_node_data)
        else:
            raise Exception("List empty")


    def remove_node(self, value):
        if self.begin:
            node = self.begin
            prev = self.begin
            while node:
                if node.value == value:
                    prev.next = node.next
                    return 
                prev = node
                node = node.next

            raise Exception("Node with data '%s' not found" % target_node_data)
        else:

            raise Exception("List is empty")
            
        
