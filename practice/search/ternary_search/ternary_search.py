class ternary_search(object):

    def __init__(self, list1):
        self.list1 = list1

    def search(self,key):
        l = 0
        r = len(self.list1)

        while l < r:
            mid1 = l + (r-l)//3
            mid2 = r - (r-l)//3

            if key == self.list1[mid1]:
                return mid1
            elif key == self.list1[mid2]:
                return mid2
            elif key < self.list1[mid1]:
                r = mid1
            elif key > self.list1[mid2]:
                l = mid2 + 1
            else:
                l = mid1+1
                r = mid2
                
        return -1        
        
        
   
