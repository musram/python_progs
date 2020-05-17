class BSTreeNode(object):
    
    def __init__(self, key, value, left=None, right=None, parent= None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        
    def find_minimum(self):
        node = self
        while node.left:
            node = node.left
        return node

    def replace_child(self, child):
        if self.parent:
            if self == self.parent.left:
                self.parent.left = child
            else:
                self.parent.right = child
        if child:
            child.parent = self.parent

                
        
        
        
        
    def __repr__(self):
        return "{}={}:<--- ({}) ---> ({})".format(self.key, self.value, self.left, self.right)


class BSTree(object):

    def __init__(self):
        self.root = None

    def set(self, key, value):
        
        if self.root:
            node = self.root
            while node:
                if node.key == key:
                    node.value = value
                    break
                elif node.key < key:
                    if node.right:
                        node = node.right
                    else:
                        node.right =  BSTreeNode(key, value, parent=node)
                elif node.key > key:
                    if node.left:
                        node = node.left
                    else:
                        node.left =  BSTreeNode(key, value, parent=node)
                else:
                    assert False, "Should not happen"
        else:

            self.root = BSTreeNode(key, value)

            
    def get(self, key):

        if self.root:
            node = self.root
            while node:
                if node.key == key:
                    return node.value
                    break
                elif node.right is None and node.left is None:
                    return None
                elif node.key < key:
                    if node.right:
                        node = node.right
                elif node.key > key:
                    if node.left:
                        node = node.left
                else:
                    assert False, "Should not happen"
        else:

            return 
         

    def  _delete(self, key, node):
         assert node , "Invalid node";
         

         if node.key < key:
             if node.right:
                self._delete(key, node.right)
             else:
                 return

         elif node.key > key:
             if node.left:
                self._delete(key, node.left)
             else:
                 return
         else:
             print(key)
             if node.left  and  node.right:
                 sucessor = find_minimum()
                 node.key = sucessor.key
                 self._delete(successor.key, successor)
             elif node.right:
                 if self.root == node:
                     self.root = node.right
                 else:
                     node.replace_child(node.right)
                 
             elif node.left:
                 print("i am here")
                 if self.root == node:
                     self.root = node.left
                 else:
                     node.replace_child(node.left)
             else:
                 if self.root == node:
                     self.root = None
                 else:
                     print("I am here")
                     node.replace_child(None)
                 
    def _delete(self, key, node):
        """Deletes the given key from the data structure."""
        assert node, "Invalid node given."

        if key < node.key:
            self._delete(key, node.left)
        elif key > node.key:
            self._delete(key, node.right)
        else:
            if node.left and node.right:
                successor = node.find_minimum()
                node.key = successor.key
                self._delete(successor.key, successor)
            elif node.right:
                if self.root == node:
                    self.root = node.right
                else:
                    node.replace_child(node.right)
            elif node.left:
                if self.root == node:
                    self.root = node.left
                else:
                    node.replace_child(node.left)
            else:
                if self.root == node:
                    self.root = None
                else:
                    node.replace_child(None)
         
    def delete(self, key):
        if self.root:
           self._delete(key, self.root)
        

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


        
        
