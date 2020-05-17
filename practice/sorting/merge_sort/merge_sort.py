import math 

def merge_sort(list_elements):
    if len(list_elements) == 1:
        return list_elements

    else:
        indx = math.floor(len(list_elements) // 2)
        list1 = merge_sort(list_elements[0 : indx])
        list2 = merge_sort(list_elements[indx : ])
       
        return merge(list1, list2)


    
def merge(list_elements1, list_elements2):

    

    result = []
    i = j = 0
    while i != len(list_elements1)   and j != len(list_elements2)  :
        if list_elements1[i] >= list_elements2[j]:
            result.append(list_elements2[j])
            j += 1
        else:
            result.append(list_elements1[i])
            i += 1
    if i != len(list_elements1):

        for indx in range(i, len(list_elements1)):
            result.append(list_elements1[indx])


    if j != len(list_elements2):

        for indx in range(i, len(list_elements2)):
            result.append(list_elements2[indx])

    return result        
        
            
