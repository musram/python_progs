from trie import *


def test_functions():
    tree = Trie()
    tree.insert("the")
    tree.insert("a")
    tree.insert("there")
    tree.insert("anaswe")
    tree.insert("any")
    tree.insert("by")
    tree.insert("their")
    #assert tree.root.children[tree._charToIndex("t")].children[tree._charToIndex("h")].children[4].children[17] != None

    assert tree.search("the") == True
    assert tree.search("these") == False
   
    assert tree.search("a") == True 
    assert tree.search("anaswe") == True
    assert tree.search("any") == True
    assert tree.search("by") == True
    assert tree.search("there") == True
    assert tree.search("thaw") == False



if __name__ == "__main__":
    test_functions()
  
