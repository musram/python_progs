from binary_search import *



def test_binary_search():

    animals = sorted(["CAT", "DOG", "RAT", "BAT", "MONKEY", "DONKEY", "DEER", "BIRDS"])

    bs = binary_search(animals)
    
    assert bs.search("SHIT") == -1
    assert bs.search("BAT") == 0
    assert bs.search("CAT") ==  2
    assert bs.search("RAT") ==  7


if __name__ == "__main__":
    test_binary_search()
