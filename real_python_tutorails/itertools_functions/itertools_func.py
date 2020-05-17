#https://florian-dahlitz.de/blog/introduction-to-itertools
#https://docs.python.org/3/library/itertools.html



if __name__ == "__main__":


    """
    Infinite iterators produce streams of infinite length (as the name suggests). Accessing them by functions or loops to truncate the streams is strongly recommended. There exist three of them in the itertools module: count(), cycle(), and repeat().
    """

    #The purpose of count() is to return an iterator, that simply starts counting at a specified number. Optionally, you can provide the step size as a second parameter.

    from itertools import count
    c = count()
    for i in range(5):
        print(next(c))


    c = count(10,2)
    for i in range(5):
        print(next(c))


    names = ["Alice", "Bob", "Larry", "Margaret"]
    names_with_index = [name for name in zip(count(1), names)]
    print(names_with_index)


    #cycle() iterates over all elements of an iterable, saves a copy and returns them. Once the iterable is exhausted, it continues infinitely returning the saved elements. To understand the function better, consider the following use case: You are teaching a class and for a group work, you want to divide the students into three teams. The following code snippet shows you a possible implementation of it using cycle().


    from itertools import cycle

    names = ["Alice", "Bob", "Chris", "Larry", "Margaret", "Naomi", "Sarah"]
    groups = cycle([1, 2, 3])
    names_with_groups = [name for name in zip(names, groups)]

    print(names_with_groups)



    #The repeat function receives an object as parameter and returns it over and over again. Optionally, you can specify the number of repetitions as a second argument. Otherwise, it repeats forever. repeat() is commonly used together with the built-in map() and zip() functions. The following example is from the itertools documentation [1]. It computes the square numbers for the numbers 0-9.

    from itertools import repeat
    list(map(pow, range(10), repeat(2)))



    #terators terminating on the shortest input sequence. As the name suggests, the functions provided in this section are terminating on the shortest input sequence. In contrast to infinite iterators, these functions do not produce infinite data streams. This group is by far the largest as it contains 12 functions:




    



    #Combinatoric iterators. The group of combinatoric iterators consists of the following four functions:


    #The permutations() function generates all possible permutations for a given length r (second argument). If r is not specified, the length of each permutation is equal to the length of the iterable specified as the first argument.




    from itertools import permutations

    l = [1, 2, 3]

    print(list(permutations(l)))

    print(list(permutations(l,2)))


    from itertools import combinations

    l = [1, 2, 3]
    m = [1 , 2, 3, 1]

    print(list(combinations(l,2)))
    print(list(combinations(l,3)))

    print(list(combinations(m,3)))

    #combinations_with_replacement() function does compute combinations which include repeated elements.


    from itertools import combinations_with_replacement

    print(list(combinations_with_replacement(m,2)))


    #In order to extend the existing itertools tool set, you can install more-itertools [5] providing high performance functions built upon the existing ones. The package is available via pip: python -m pip install more-itertools

    """
    # more_itertools_flatten.py

    from more_itertools import flatten

    nested_list = [[1, 2], [3, 4]]
    flattened_list = list(flatten(nested_list))

    print(flattened_list)

    """

