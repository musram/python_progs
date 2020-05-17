class Node(object):
    def __init__(self, key, value,left=None,  right=None, parent = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
       return self.value


class bst(object):
    
   def __init__(self):
       self.root = None

   def set(self, key,  value):
       if self.root:
          node = self.root 
          while node:
              if node.key == key:
                 node.value = value
                 break
              elif node.left is None and node.right is None:
                 if node.key > key:
                     node.left = Node(key, value, parent=node)
                 else:
                     node.right = Node(key, value, parent=node)
              elif node.key < key:
                  if node.right:
                     node = node.right
                  else:
                     node.right = Node(key, value, parent=node) 
              elif node.key > key:
                  if node.left:
                     node = node.left
                  else:
                     node.left = Node(key, value, parent=node)
              else:
                  raise Exception("Should not happen")
                  
           
       else:
           self.root = Node(key, value, parent=self.root)


           
   def get(self, key):
       if self.root:
           node = self.root
           while node:
               if node.key == key:
                   return node.value
               elif node.right is None and node.left is None:
                   return 
               elif node.key > key:
                   node = node.left
               elif node.key < key:
                   node = node.right
       else:
           return

   def _list(self, node, indent=0):
        """List the elements in the tree."""
        assert node, "Invalid node given."

        if node:
            print(" " * indent, node.key,"=", node.value)

            if node.left:
                print(" " * indent, "<", end="")
                self._list(node.left, indent+1)
            if node.right:
                print(" " * indent, ">", end="")
                self._list(node.right, indent+1)

   def list(self, start=""):
        print("\n\n----", start)
        self._list(self.root)
    
