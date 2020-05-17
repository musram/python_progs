from trie import *



class SuffixTrie(Trie):
    def __init__(self):
        super().__init__()

    def isSubString(self, key):
        node = self.root
        for level in range(len(key)):
            idx =self. _charToIndex(key[level])
            if not  node.children[idx]:
                return False
            node = node.children[idx]
        return  node is not None or node.isEndOfWord

    def isSuffix(self, key):
        return super().search(key)

    def count(self, key):
        node = self.root
        for level in range(len(key)):
            idx =self. _charToIndex(key[level])
            if not  node.children[idx]:
                return -1
            node = node.children[idx]
        return len([k for k in node.children  if k is not None])
