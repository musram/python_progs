
from my_tstree import *


def test_TSTree_get_set():
    urls = TSTree()
    urls.set("/apple/", "Apple")
    urls.set("/grape/", "Grape")
    urls.set("/kiwi/", "Kiwi")
    urls.set("/kumquat/", "Kumquat")
    urls.set("/pineapple/", "Pineapple")

    assert urls.get("/apple/") == "Apple"
    assert urls.get("/grape/") == "Grape"
    assert urls.get("/kiwi/") == "Kiwi"
    assert urls.get("/") == None

    return urls

def test_TSTree_find_all():
    urls = test_TSTree_get_set()
    results = [ n.value for n in urls.find_all("/k")]
    print(results)
    assert results == ['Kiwi', 'Kumquat']



if __name__ == "__main__":
    test_TSTree_get_set()
    test_TSTree_find_all()

    
