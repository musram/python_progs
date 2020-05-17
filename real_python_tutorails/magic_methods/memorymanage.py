


if __name__ == "__main__":
    import sys

    '''
    reference count
    The main garbage collection mechanism in CPython is through reference counts. Whenever you create an object in Python,
    the underlying C object has both a Python type (such as list, dict, or function) and a reference count. At a very basic level, a Python objects
    reference count is incremented whenever the object is referenced, and its decremented when an object is dereferenced. If an objects reference count is 0, 
    the memory for the object is deallocate.
    '''

    '''
    Every python object holds three things

    (1) object type
    (2) object value
    (3) object reference counter
    '''
    
    a = "my_string"   #Assigning an object to a variable.
    print(sys.getrefcount(a))  #Passing the object as an argument to a function.
    b = [a]   #Adding an object to a data structure, such as appending to a list or adding as a property on a class instance.
    c = {'key' :a} #Adding an object to a data structure, such as appending to a list or adding as a property on a class instance.

    print(sys.getrefcount(a))


    b = 100
    c = 200

    print(sys.getrefcount(b))
    print(sys.getrefcount(c))    
    
