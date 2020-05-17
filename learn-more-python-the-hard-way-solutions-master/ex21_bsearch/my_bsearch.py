import dllist
import bstree



def _search(data, elem , low, high):
    if low  >= high:
        return None, -1

    mid = (high - low) // 2 + low
    mid_val = data[mid]

    if elem > mid_val:
        return _search(data, elem, mid+1, high)
    elif elem < mid_val:
        return _search(data, elem, low, mid)
    elif elem == mid_val:
        return elem , mid

def search_list(data, elem):
    return _search(data, elem , 0, len(data))


def search_bstree(data,  elem):
    tree = bstree.BSTree()
    for i, key in enumerate(data):
        tree.set(key, i)

    ind = tree.get(elem)
    return ind !=None and (elem , ind) or (None, -1)
        
    
def search_dllist(data, elem):
    dlist = dllist.DoubleLinkedList()
    for key in data:
        dlist.push(key)

    low = 0
    high = dlist.count()

    while low < high :
        mid = (high - low) //2 + low
        mid_val = dlist.get(mid)

        if mid_val < elem:
             low = mid + 1
        elif mid_val > elem:
             high = mid
        else:
            return elem , mid
    return None, -1    
