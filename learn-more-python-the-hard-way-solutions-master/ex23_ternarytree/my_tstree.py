class TSTreeNode(object):
    
    def __init__(self, char, key, value, low, eq, high):
        self.char = char
        self.key = key
        self.low = low
        self.eq = eq
        self.high = high
        self.value = value

    def __repr__(self):
        return "{}:{}<{} and {}={} and {}={} and {}>".format(self.key, self.value, self.low, self.low.key, self.eq, self.eq.key, self.high, self.high.key)

class TSTree(object):

    def __init__(self):
        self.root = None

    def _get(self, node, chars):
        char = chars[0]
        if node == None:
            return None
        elif char < node.char:
            return self._get(node.low, chars)
        elif char == node.char:
            if len(chars) > 1:
                return self._get(node.eq, chars[1:])
            else:
                return node
        else:
            return self._get(node.high, chars)

    def get(self, key):
        chars = [ord(x) for x in key]
        node = self._get(self.root, chars)
        return node and node.value or None

    def _set(self, node, chars, key, value):
        next_char = chars[0]

        if not node:
            # what happens if you add the value here?
            node = TSTreeNode(next_char, None, None, None, None, None)

        if next_char < node.char:
            node.low = self._set(node.low, chars, key, value)
        elif next_char == node.char:
            if len(chars) > 1:
                node.eq = self._set(node.eq, chars[1:], key, value)
            else:
                # what happens if you DO NOT add the value here?
                node.value = value
                node.key = key
        else:
            node.high = self._set(node.high, chars, key, value)

        return node

    def set(self, key, value):
        chars = [ord(x) for x in key]
        self.root = self._set(self.root, chars, key, value)

    def _find_all(self, match , node, result):
         if not node:
             return 
         if node.key and node.value:
             result.append(node)
         if node.low:
             self._find_all(match , node.low, result)
         if node.eq:
              self._find_all(match, node.eq, result)
         if node.high:
              self._find_all(match, node.high, result)
       
        
        
        
    def find_all(self, match):
        results = []
        chars = [ord(x) for x in match]
        start = self._get(self.root, chars)
        if start:
           self._find_all( match,start.eq, results)
        return results   
           


    def find_longest(self, match):
        nodes  = self.find_all(match)
        *x, longest  = sorted(nodes, key = lambda x : len(x))
        return longest

        
    def find_shortest(self, match):
        nodes  = self.find_all(match)
        shortest, *x  = sorted(nodes, key = lambda x : len(x))
        return shortest

