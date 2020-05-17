from my_sllist import *

def test_push():
    colors = SingleLinkedList()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2
    colors.push("Ultramarine Violet")
    assert colors.count() == 3

def test_pop():
    colors = SingleLinkedList()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None

def test_unshift():
    colors = SingleLinkedList()
    colors.push("Viridian")
    colors.push("Sap Green")
    colors.push("Van Dyke")
    assert colors.unshift() == "Viridian"
    assert colors.unshift() == "Sap Green"
    assert colors.unshift() == "Van Dyke"
    assert colors.unshift() == None    


def test_shift():
    colors = SingleLinkedList()
    colors.shift("Cadmium Orange")
    assert colors.count() == 1
    colors.shift("Carbazole Violet")
    assert colors.count() == 2
    assert colors.pop() == "Cadmium Orange"
    assert colors.count() == 1
    assert colors.pop() == "Carbazole Violet"
    assert colors.count() == 0    
def test_first():
    colors = SingleLinkedList()
    colors.push("Cadmium Red Light")
    assert colors.first() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.first() == "Cadmium Red Light"
    colors.shift("Pthalo Green")
    assert colors.first() == "Pthalo Green"
    
if __name__ == '__main__':
    test_push()
    test_pop()
    test_shift()
