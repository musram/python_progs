
"""
Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator


youll see that Python zip operations work just like the physical zipper on a bag or pair of jeans. Interlocking pairs of teeth on both sides of the zipper are pulled together to close an opening
"""


if __name__ == "__main__":
    numbers = [1,2,3]
    letters = ['a','b','c']

    zipped = zip(numbers, letters)

    print(type(zipped))

    print(zipped)

    print(list(zipped))


    #when the iterables are unordered

    s1 = {2, 3, 1}
    s2 = {'b', 'a', 'c'}


    zipped = zip(s1, s2)

    print(list(zipped))  # the elements are paired randomly

    print(list(zip()))

    print(list(zip(numbers)))

    floats = [4.0, 5.0, 6.0]

    print(list(zip(numbers, letters, floats)))

    #Passing Arguments of Unequal Length
    print(list(zip(range(5), range(10))))

    from itertools import zip_longest

    longest = range(10)

    print(list(zip_longest(numbers, letters, longest, fillvalue='?')))


    for l,m, in zip(letters, numbers):
        print(l,m, sep=",")

    #unzipping is done by zip_longest

    pairs = list(zip(numbers, letters))

    a, b = zip(*pairs)

    print(a)
    print(b)

    #building dictionary

    fields = ['name', 'last_name', 'age', 'job']
    values = ['John', 'Doe', '45', 'Python Developer']


    a_dict = dict(zip(fields, values))

    new_job = ['Python Consultant']
    field = ['job']

    a_dict.update(zip(field, new_job))

    print(a_dict)
