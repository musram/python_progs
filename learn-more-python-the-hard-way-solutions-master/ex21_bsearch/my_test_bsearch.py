import my_bsearch




def test_bsearch_list():
    data = sorted([4,2,5,6,7,22,301])
    assert my_bsearch.search_list(data, 5) == (5, 2)
    assert my_bsearch.search_list(data, 301) == (301, len(data)- 1)
    assert my_bsearch.search_list(data, 4) == (4, 1)
    assert my_bsearch.search_list(data, 6) == (6, 3)
    assert my_bsearch.search_list(data, 200) == (None, -1)
    assert my_bsearch.search_list(data, -1) == (None, -1)


def test_bstree_search():
    data = sorted([4,2,5,6,7,22,301])
    assert my_bsearch.search_bstree(data, 5) == (5, 2)
    assert my_bsearch.search_bstree(data, 301) == (301, len(data)- 1)
    assert my_bsearch.search_bstree(data, 4) == (4, 1)
    assert my_bsearch.search_bstree(data, 6) == (6, 3)
    assert my_bsearch.search_bstree(data, 200) == (None, -1)
    assert my_bsearch.search_bstree(data, -1) == (None, -1)
    

def test_bstree_dllist():
    data = sorted([4,2,5,6,7,22,301])
    assert my_bsearch.search_dllist(data, 5) == (5, 2)
    assert my_bsearch.search_dllist(data, 301) == (301, len(data)- 1)
    assert my_bsearch.search_dllist(data, 4) == (4, 1)
    assert my_bsearch.search_dllist(data, 6) == (6, 3)
    assert my_bsearch.search_dllist(data, 200) == (None, -1)
    assert my_bsearch.search_dllist(data, -1) == (None, -1)
    


if __name__ == "__main__":
    test_bsearch_list()
    test_bstree_search()
    test_bstree_dllist()

    
