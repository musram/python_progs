from random import randint
from timeit import repeat
from math import floor

def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")



def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]

        j = i -1

        while( j >=0 and array[j] > key_item):
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key_item
    return array    




def merge_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))    
    
def merge(left, right):

    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []

    left_index = right_index = 0

    if len(result) < len(right) + len(left):

        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:    
            result.append(right[right_index])
            right_index += 1

        if left_index == len(left):
            result +=  right[right_index:]

        if right_index == len(right):
            result +=  left[left_index:]

    return result        

        


    
    



ARRAY_LENGTH = 100




if __name__ == "__main__":
    array = [8, 2, 6, 4, 5]

    #assert insertion_sort(array) == [2,4,5,6,8]

    print(merge_sort(array))

    assert merge_sort(array) == [2,4,5,6,8]
    

    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    run_sorting_algorithm(algorithm="insertion_sort", array=array)
        
        
        
