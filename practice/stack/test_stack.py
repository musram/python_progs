from stack import *



def test_stack_push():
    animals = Stack()
    animals.push("CAT")
    assert animals.top.value == "CAT"
    animals.push("DOG")
    assert animals.top.value == "DOG"
    return animals
    
def test_stack_pop():
    animals = test_stack_push()
    assert animals.pop() == "DOG"
    assert animals.pop() == "CAT"
    assert animals.pop() ==  None

def test_stack_count():
    animals = Stack()
    animals.push("CAT")
    animals.push("DOG")
    animals.push("RAT")
    animals.push("BAT")
    assert animals.count() == 4
    assert animals.pop() == "BAT"
    assert animals.pop() == "RAT"
    assert animals.count() == 2
    




if __name__ == "__main__":
    test_stack_push()
    test_stack_pop()
    test_stack_count()
