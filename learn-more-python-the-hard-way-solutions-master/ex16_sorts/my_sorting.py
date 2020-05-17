
from dllist import DoubleLinkedList

def bubble_sort(numbers):
    while True:
       is_sorted = True
       node = numbers.begin.next
       while node:
           if node.prev.value > node.value:
               node.prev.value , node.value = node.value, node.prev.value
               is_sorted = False
           node = node.next    
       if is_sorted:
           break
       
