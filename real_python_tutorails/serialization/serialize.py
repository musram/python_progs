###https://realpython.com/python-pickle-module/


#serialization allows you to take a complex object structure and transform it into a stream of bytes that can be saved to a disk or sent over a network. The marshal module, The json module, The pickle module  are modules for serialization.


#pickel module

# pickle.dump(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None)
# pickle.dumps(obj, protocol=None, *, fix_imports=True, buffer_callback=None)
#pickle.load(file, *, fix_imports=True, encoding="ASCII", errors="strict", buffers=None)
#pickle.loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict", buffers=None)


#The only difference between dump() and dumps() is that the first creates a file containing the serialization result, whereas the second returns a string.The same concept also applies to load() and loads(): The first one reads a file to start the unpickling process, and the second one operates on a string.



if __name__ == "__main__" :

    import pickle

    class example_class:
        a_number = 35
        a_string = "hey"
        a_list = [1, 2, 3]
        a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
        a_tuple = (22, 23)

    my_object = example_class()

    my_pickled_object = pickle.dumps(my_object)  # Pickling the object
    print("This is my pickled object:\n{}\n".format(my_pickled_object))

    my_object.a_dict = None

    my_unpickled_object = pickle.loads(my_pickled_object)  # Unpickling the object
    print("This is a_dict of the unpickled object:\n{}\n".format(my_unpickled_object.a_dict))

