from ternary_search import *



def test_ternary_search():

    animals = sorted(["CAT", "DOG", "RAT", "BAT", "MONKEY", "DONKEY", "DEER", "BIRDS"])

    bs = ternary_search(animals)
    
    
    assert bs.search("BAT") == 0
    assert bs.search("CAT") ==  2
    assert bs.search("RAT") ==  7
    assert bs.search("SHIT") == -1

if __name__ == "__main__":
    test_ternary_search()
