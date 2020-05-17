from cir_linked_list import *



def test_circular_list_insert():
    animals = CircularLinkedList()
    animals.insert("CAT")
    assert animals.head.value == "CAT"
    animals.insert("DOG")
    assert animals.head.value == "CAT"
    animals.insert("RAT")
    animals.head.value == "CAT"
    assert animals.head.next.next.next.value == "CAT"
    return animals
  
def test_cirular_list_delete():
    animals = test_circular_list_insert()
    animals.delete()
    assert animals.head.value == "DOG"
    animals.delete()
    assert animals.head.value == "RAT"
    animals.delete()
    assert animals.head == None
    

    

if __name__ == "__main__":
    test_circular_list_insert()
    test_cirular_list_delete()
