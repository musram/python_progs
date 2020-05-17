from linked_list import *


def test_linked_list_add_last():
    animals = LinkedList()
    animals.add_last("CAT")
    assert animals.begin.value == "CAT"
    animals.add_last("DOG")
    print(animals)
    assert animals.begin.value == "CAT"
    assert animals.begin.next.value == "DOG"
    return animals



def test_linked_list_add_first():
    animals = LinkedList()
    animals.add_first("CAT")
    assert animals.begin.value == "CAT"
    animals.add_first("DOG")
    assert animals.begin.value == "DOG"
    assert animals.begin.next.value == "CAT"
    return animals

def test_linked_list_add_after():
    animals = test_linked_list_add_first()
    print(animals)
    animals.add_after("DOG", "RAT")
    assert animals.begin.value == "DOG"
    assert animals.begin.next.value == "RAT"
    assert animals.begin.next.next.value == "CAT"
    print(animals)

def test_linked_list_add_before():
    animals = test_linked_list_add_first()
    animals.add_before("CAT", "RAT")
    assert animals.begin.value == "DOG"
    assert animals.begin.next.value == "RAT"
    assert animals.begin.next.next.value == "CAT"
    return animals

    
def test_linked_list_remove():
    animals = test_linked_list_add_before()
    animals.remove_node("RAT")
    print(animals)
    assert animals.begin.value == "DOG"
    assert animals.begin.next.value == "CAT"
    
    


if __name__ == "__main__":
    test_linked_list_add_last()    
    test_linked_list_add_first()
    test_linked_list_add_after()
    test_linked_list_add_before()
    test_linked_list_remove()
    
    
