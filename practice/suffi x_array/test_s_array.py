from s_array import *

def test_print():
    array = SuffixArray("abracadabra")
    print(array)


def test_s_array_search():
    finder = SuffixArray("abracadabra")
    assert finder.search("bra") == (5, 8)
    assert finder.search("ra") == (9,9)
    assert finder.search("abra") == (1,7)
    assert finder.search("cadabra") == (7,4)


    assert finder.find_shortest("abra") == 7
    assert finder.find_shortest("a") == 10

  
    assert finder.find_longest("a") == ("abracadabra", 0)
    assert finder.find_longest("bra") == ("bracadabra", 1)

    assert finder.find_all("bra") == [('bra', 8), ('bracadabra', 1)]
    assert finder.find_all("ra") == [('ra', 9), ('racadabra', 2)]




if __name__ == "__main__":
    test_print()
    test_s_array_search()
    
