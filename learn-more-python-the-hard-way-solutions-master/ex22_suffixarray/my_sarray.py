
class SuffixArray(object):

      def __init__(self, instr):
        self.instr = instr
        self.sarray = sorted([ (self.instr[i:], i) for i in range(len(self.instr))])


      def __repr__(self):
      	  return '[' +  ' '.join(list(map(lambda x : x[0], self.sarray))) + ']'


      def search(self, elem):
            low = 0
            high = len(self.sarray)

            while low < high :
                  mid = (high - low) // 2  + low

                  mid_val, starts_at = self.sarray[mid]

                  if mid_val > elem:
                        high = mid
                  elif mid_val < elem:
                        low = mid + 1
                  else:
                        return mid, starts_at
                  
            return -1, -1

      def find_shortest(self, elem):
           _, start_at = self.search(elem)
           return start_at


      def find_longest(self, elem):
           
           sarray_i, inst_i = self.search(elem)
           if sarray_i == -1:
                 return -1, -1

           test, inst_i   = self.sarray[sarray_i]
           longest, longest_i = test, inst_i
           for ind in range(sarray_i, len(self.sarray)):
                 
                 test, inst_i = self.sarray[ind]
             
                 if test.startswith(elem):
                       if len(test) > len(longest):
                             longest, longest_i  = test, inst_i

           return longest, longest_i                  
                       
                 
      def  find_all(self, elem):

           sarray_i, inst_i = self.search(elem)
           if sarray_i == -1:
                 return -1, -1

          
           all_list = []
           for ind in range(sarray_i, len(self.sarray)):
                 test, inst_i = self.sarray[ind]
                 if test.startswith(elem):
                     all_list.append((test, inst_i))
                     
           return all_list
