from queue import *


def test_queue_enque():
    animals = Queue()
    animals.enque("CAT")
    assert animals.rear.value == "CAT"
    animals.enque("DOG")
    assert animals.rear.value == "DOG"
    animals.enque("RAT")
    assert animals.rear.value == "RAT"
    return animals

def test_queue_deque():
    animals = test_queue_enque()
    animals.deque() == "CAT"
    animals.deque() == "DOG"
    animals.deque() == "RAT"
    animals.deque() == "None"


if __name__ == "__main__" :
    test_queue_enque()
    test_queue_deque()
    
    
    
