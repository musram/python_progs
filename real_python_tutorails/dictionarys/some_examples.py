#https://realpython.com/python-defaultdict/#handling-missing-keys-in-dictionaries


if __name__ == "__main__":
    d = {}

    #handling missing keys
    #(1) setdefault
    """
    setdefault(key[, default])

    If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.
     """
    default = d.setdefault('misssing_key', 'default_value')
    print(default)

    print(d['misssing_key'])


    """
    (2) get(key[, default])

    Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError

    """
    d = {}
    default = d.get('missing_key', 'default value')
    print(default)
    print(d)

    #(3) in method

    d = {}
    if 'key' in d:
        print(d['key'])
    else:
        d['key'] = 'default_value'

    print(d)

    #(4) try except

    try:
        print(d['key'])
    except KeyError as e:
        d['key'] = 'default_value'

    print(d)


    

    #defaultdict

    from collections import defaultdict

    print(issubclass(defaultdict, dict))

    print(set(dir(defaultdict)) - set(dir(dict)))
    
    std_dict = dict(numbers=[1, 2, 3], letters=['a', 'b', 'c'])

    def_dict = defaultdict(list, numbers=[1, 2, 3], letters=['a', 'b', 'c'])

    print(std_dict == def_dict)

    #The first argument to the Python defaultdict type must be a callable that takes no arguments and returns a value. This argument is assigned to the instance attribute, .default_factory.

    dd = defaultdict(list, letters=['a', 'b', 'c'])

    print(dd.default_factory)

    print(dd)

    print(dd['missing_key'])

    dd['missing_key'].append(1)

    print(dd)

    dd['letters'] += [2,3]

    print(dd)

    """
    Keep in mind that .default_factory is only called from .__getitem__() and not from other methods. This means that if dd is a defaultdict and key is a missing key, then dd[key] will call .default_factory to provide a default value, but dd.get(key) still returns None instead of the value that .default_factory would provide. Thats because .get() doesnt call .__getitem__() to retrieve the key
    """

    """
    .__copy__()	Provides support for copy.copy()
    .default_factory	Holds the callable invoked by .__missing__() to automatically provide default values for missing keys
    .__missing__(key)	Gets called when .__getitem__() canxt find key
    """
    
    dd = defaultdict(list)

    print(dd['missing'])

    print(dd.get('another_missing'))  #doesnot call __getitem__

    print(dd)

    #change or update the callable

    dd.default_factory = str
    print(dd['missing_key'])
    print(dd)

    """
    At this point, you may have an idea of when to use a defaultdict rather than a regular dict. Here are three things to take into account:

If your code is heavily base on dictionaries and youre dealing with missing keys all the time, then you should consider using a defaultdict rather than a regular dict.

If your dictionary items need to be initialized with a constant default value, then you should consider using a defaultdict instead of a dict.

If your code relies on dictionaries for aggregating, accumulating, counting, or grouping values, and performance is a concern, then you should consider using a defaultdict.
    """



    import collections

    class my_defaultdict(collections.UserDict):
        def __init__(self, default_factory=None, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if not callable(default_factory) and default_factory is not None:
                raise TypeError('first argument must be callable or None')
            self.default_factory = default_factory

        def __missing__(self, key):
            if self.default_factory is None:
                raise KeyError(key)
            if key not in self:
                self[key] = self.default_factory()
            return self[key]

    dd_one = my_defaultdict(list)
    print(dd_one)
    dd_one['missing']
    print(dd_one)
    dd_one.default_factory = int
    dd_one['another_missing']
    print(dd_one)

    dd_two = my_defaultdict(None)
    try:
        dd_two['missing']
    except KeyError as e:
        print(e)


    #subclassing
    """
    the main reason for this is that subclassing built-in types can be error-prone because the C code of the built-ins doesnt seem to consistently call special methods overridden by the user.
    """

    class MyDict(dict):
        def __setitem__(self, key, value):
            super().__setitem__(key, None)

    my_dict = MyDict(first=1)  #does not call __setitem__
    print(my_dict)

    my_dict['second'] = 2     #calls __setitem__
    print(my_dict)

    my_dict.setdefault('third', 3)
    print(my_dict)  #notice that .setdefault() doesnt call .__setitem__() either, because your third key ends up with a value of 3.

    """
    UserDict is a more reliable class when it comes to creating custom mappings
    """

    class my_defaultdict(collections.UserDict):
    # Snip
        def __init__(self, default_factory=None, *args, **kwargs):
            super().__init__(*args, **kwargs)
        
        def __setitem__(self, key, value):
            print('__setitem__() gets called')
            super().__setitem__(key, None)

    my_dict = my_defaultdict(list, first=1)   #calls __setitem__
    print(my_dict)

    my_dict['second'] = 2     #calls __setitem__
    print(my_dict)

    my_dict.setdefault('third', 3)   #calls __setitem__
    print(my_dict)

    
    
    
    
