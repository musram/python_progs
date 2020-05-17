

class binary_search(object):

    def __init__(self, list1):
        self.list1 = list1

    def search(self, key):    
        low = 0
        high = len(self.list1)

        while low < high:
            mid = (high - low) //2 + low
            mid_val = self.list1[mid]

            if mid_val == key:
                return mid
            elif mid_val < key:
                low = mid + 1
            else:
                high = mid
        return -1        
        
