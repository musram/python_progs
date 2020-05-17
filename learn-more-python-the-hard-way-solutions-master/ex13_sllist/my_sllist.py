class SingleLinkedListNode(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __repr__(self):
        nval = self.next and self.next.value or None
        return '[{}:{}]'.format(self.value, self.next)

class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        node = SingleLinkedListNode(obj, None)
        if self.begin == None:
            # nothing net
            self.begin = node
            self.end = self.begin
        else:
            self.end.next = node
            self.end = node
            assert self.begin != self.end

        assert self.end.next == None

    def pop(self):
        """Removes the last item and returns it."""
        if self.end == None:
            return None
        elif self.end == self.begin:
            node = self.begin
            self.end = self.begin = None
            return node.value
        else:
            node = self.begin
            while node.next != self.end:
                node = node.next
            assert self.end != node
            self.end = node
            return node.next.value

    def shift(self, obj):
        """Another name for push."""
        return self.push(obj)
    
    def unshift(self):
        """Removes the first item and returns it."""

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""

    def count(self):
        """Counts the number of elements in the list."""
        node = self.begin
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def get(self, index):
        """Get the value at index."""

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""

