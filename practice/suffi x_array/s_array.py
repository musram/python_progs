class SuffixArray(object):
    def __init__(self, string):
        self.sfx_array = sorted([(string[i:], i) for i in range(len(string))], key= lambda x : x[0])

    def __repr__(self):
        return '[' + ','.join([s[0] for s in self.sfx_array]) + ']'


    def search(self, string):
        low = 0
        high = len(self.sfx_array)

        while low < high :
            mid = (high - low) // 2 + low
            mid_val, starts_at = self.sfx_array[mid]

            if mid_val > string:
                high = mid
            elif mid_val < string:
                low = mid + 1
            else:
                return (mid, starts_at)
        return -1, -1    

    
    def find_shortest(self, string):
       _, starts_at = self.search(string)
       return starts_at

    def find_longest(self, string):
        sarray_i , inst_i = self.search(string)
        if sarray_i == -1:
            return -1, -1

        longest, longest_i = self.sfx_array[sarray_i]

        for s in range(sarray_i, len(self.sfx_array)):
            test, starts_at = self.sfx_array[s]
            if test.startswith(string):
               if len(test) > len(longest):
                  longest, longest_i = test, starts_at

        return longest, longest_i


    def find_all(self, string):
       
        sarray_i, inst_i = self.search(string)
        if sarray_i == -1:
            return -1, -1

        results = []
        for s in range(sarray_i, len(self.sfx_array)):
            test, starts_at = self.sfx_array[s]
            if test.startswith(string):
               results.append((test, starts_at))
 
        return results
        
