class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev
    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return '[{}, {}, {}]'.format(self.value, repr(nval), repr(pval))

class DoubleLinkedList(object):
    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, value):
       if self.begin:
           node = DoubleLinkedListNode(value, None, self.end)
           self.end.next = node
           self.end = node
       else:
           self.begin = self.end  = DoubleLinkedListNode(value, None, None)

    def pop(self):
        if self.begin:
            node = self.end   
            if self.begin == self.end:
                self.begin = self.end = None
            else:
                self.end = node.prev
                self.end.next = None
                if self.begin == self.end:
                    self.begin.prev = None
            return node.value
        else:
            return

    def shift(self, value):
        self.push(value)

    def unshift(self):
        if self.begin:
            node = self.begin   
            if self.begin == self.end:
                self.begin = self.end = None
            else:
                self.begin = node.next
                self.begin.prev = None
                if self.begin == self.end:
                    self.end.next = None
            return node.value
        else:
            return
        
    def get(self, index):
        node = self.begin
        i = 0
        while node:
            if i == index:
                return node.value
            else:
                i += 1
                node = node.next
        return     

    def detach_node(self, node):
        if self.end == node:
            self.pop()
        elif self.begin == node:
            self.unshift()
        else:
            node.prev.next = node.next.prev
            node.next.prev = node.prev.next
            
    
    def remove(self, value):
        node = self.begin
        count = 0
        while node:
            if node.value == value:
                self.detach_node(node)
                return count
            else:
                count += 1
                node = node.next
        return -1         
        
        
    def first(self):
        if self.begin:
           return self.begin.value
        else:
           return
    def last(self):
        return self.end and self.end.value or None
    
    def count(self):
        counter = 0
        node = self.begin
        while node:
            node = node.next
            counter += 1
        return counter    

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        # set node to begin
        node = self.begin
        print(">>>> ", end="")
        # while there's a node, print it out
        while node:
            print(node, end="")
            node = node.next
        # print new line
        print()

    def _invariant(self):
        if self.begin is None:
            assert self.end == None, "End set while begin is not."

        if self.begin:
             assert self.begin.prev == None , "begin.prev not None"
             assert self.end.next == None ,  "end.next not None"

        if self.count() == 1:
            assert self.begin == self.end ,  "one element"
