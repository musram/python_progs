"""
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
Implementation of the iterator pattern with a generator
*TL;DR
Traverses a container and accesses the container's elements.
"""


def count_to(count):
    """Counts by word numbers, up to a maximum of five"""
    numbers = ["one", "two", "three", "four", "five"]
    for num in numbers[:count]:
        yield num

count_to_five = lambda: count_to(5)
count_to_two = lambda: count_to(2)        



class NumberWords:
    """Counts by word numbers, up to a maximum of five"""
    _WORD_MAP = (
        'one',
        'two',
        'three',
        'four',
        'five',
    )

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if (self.start > self.stop) or (self.start > len(self._WORD_MAP)):
            raise StopIteration
        current = self.start
        self.start += 1
        return self._WORD_MAP[current -1 ]
    
            


if __name__ == "__main__":
    for i in count_to_five():
        print(i)

    for i in count_to_two():
        print(i)        

    for number in NumberWords(start=1, stop=2):
        print(number)        
