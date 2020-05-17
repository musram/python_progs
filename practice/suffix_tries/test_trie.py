from suffix_trie import *


def test_functions():
    tree = SuffixTrie()
    key = "abaaba"
    for i in range(len(key)):
       tree.insert(key[i:])
    
    assert tree.search("ba") == True
    assert tree.search("aba") == True
    assert tree.search("aa") == False

    assert tree.isSubString("aa") == True
    assert tree.isSubString("abaaba") == True
    assert tree.isSubString("aaaba") == False

    assert tree.isSuffix("ba") == True
    assert tree.isSuffix("aba") == True
    assert tree.isSuffix("aa") == False

    assert tree.count("a") == 2
    
    
    
    
   

if __name__ == "__main__":
    test_functions()
  
