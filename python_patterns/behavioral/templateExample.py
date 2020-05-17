#http://34.212.143.74/s201911/pycon2019/docs/design_patterns.html#_singleton_pattern
#https://refactoring.guru/design-patterns/template-method

from abc import ABC, abstractmethod

class AverageCalculator(ABC): 

    def average(self): 
        try:
            num_items = 0
            total_sum = 0
            while self.has_next():
                total_sum += self.next_item()
                num_items += 1
            if num_items == 0:
                raise RuntimeError("Can't compute the average of zero items.")
            return total_sum / num_items
        finally:
            self.dispose()

    @abstractmethod
    def has_next(self): 
        pass

    @abstractmethod
    def next_item(self): 
        pass

    def dispose(self): 
        pass


class FileAverageCalculator(AverageCalculator):

    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename)
        self.last_line = self.file.readline()

    def has_next(self):
        return self.last_line != ''

    def next_item(self):
        if self.has_next():
            result = float(self.last_line)
            self.last_line = self.file.readline()
            return result

    def dispose(self):
        self.file.close()

class MemoryAverageCalculator(AverageCalculator):

    def __init__(self, list1):
        self.list1 = list1
        self.last_elem = self.list1.pop()

    def has_next(self):
        return len(self.list1) > 0

    def next_item(self):
        if self.has_next():
            result = self.last_elem
            self.last_elem = self.list1.pop()
            return result

    def dispose(self):
        del self.list1 
    


if __name__ == "__main__":
    fac = FileAverageCalculator('data.txt')
    print(fac.average())

    mac = MemoryAverageCalculator([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
    print(mac.average())        
