class TrieNode(object):
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

    def  _repr_(self):
        return '[' + ','.join(self.children) + ']'


class Trie(object):
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        node = self.root
        for level in range(len(key)):
            idx =self. _charToIndex(key[level])
            if not node.children[idx]:
                node.children[idx] = self.getNode()
            node = node.children[idx]
        node.isEndOfWord = True

        
    def search(self, key):
        node = self.root
        for level in range(len(key)):
            idx =self. _charToIndex(key[level])
            if not  node.children[idx]:
                return False
            node = node.children[idx]
        return node  and node.isEndOfWord

    
    
            
 
