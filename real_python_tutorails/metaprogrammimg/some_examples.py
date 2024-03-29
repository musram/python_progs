#https://nikolanews.com/metaprogramming-in-python/
#https://developer.ibm.com/technologies/analytics/tutorials/ba-metaprogramming-python/


if __name__ == "__main__":
    class SomeClass:
        pass

    some_obj = SomeClass()

    import inspect

    print(inspect.isclass(SomeClass))
    print(inspect.isclass(some_obj))
    print(inspect.isclass(some_obj.__class__))

    print(type(SomeClass))

    print(type(type(SomeClass)))

    print(inspect.isclass(type(SomeClass)))

    print(inspect.isclass(type(type(SomeClass))))

    """
    Everything is an object in Python, and they are all either instances of
classes or instances of metaclasses, except for type.

    So now we know that an instance is an instantiation class, and class is an
instance of a metaclass.
    """

    print(isinstance(some_obj, SomeClass))
    print(isinstance(SomeClass, type))

    """
    type is itself a class, and it is its own type. Its a
metaclass. A metaclass instantiates and defines behavior for a class just
like a class instantiates and defines behavior for an instance.

type is the built-in metaclass Python uses. To change the
behavior of classes in Python (like the behavior of
SomeClass), we can define a custom metaclass by inheriting
the type metaclass. Metaclasses are a way to do
metaprogramming in Python.
    """


    """
    Heres what happens whenever the keyword class is encountered:

    (1) The body (statements and functions) of the class is isolated.
    (2) The namespace dictionary of the class is created (but not populated
yet).
    (3) The body of the class executes, then the namespace dictionary is
populated with all of the attributes, methods defined, and some
additional useful info about the class.
    (4) The metaclass is identified in the base classes or the metaclass hooks
(explained later) of the class to be created.
    (5) The metaclass is then called with the name, bases, and attributes of
the class to instantiate it.
    """

    """
    And because type is the default metaclass in Python, you can
use type to create classes in Python.
    """

    SomeClass = type('SomeClass', (), {}) #  same as class SomeClass: pass

    class ParentClass:
        pass

    class SomeClass(ParentClass):
        some_var = 5
        def some_function(self):
            print("Hello!")
    
    # the above is  same as

    def some_function(self):
        print("Hello!")

    ParentClass = type('ParentClass', (), {})
    SomeClass = type('SomeClass', (ParentClass, ), {'some_function':some_function, 'some_var':5})


    some_obj = SomeClass()
    some_obj.some_function()


    #decorator application

    from functools import wraps
    import random
    import time

    def wait_random(min_wait=1, max_wait=30):
        def inner_function(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                time.sleep(random.randint(min_wait, max_wait))
                return func(*args, **kwargs)

            return wrapper

        return inner_function

    @wait_random(10, 15)
    def function_to_scrape():
        # some scraping stuff
        pass

    # what happens here?
    class Scraper:
        def func_to_scrape_1(self):
            # some scraping stuff
            pass
        def func_to_scrape_2(self):
            # some scraping stuff
            pass
        def func_to_scrape_3(self):
            # some scraping stuff
            pass    

    #The idea is to walk through the class namespace, identify the functions, and wrap them with our decorator.


    print(vars(Scraper))
    def classwrapper(cls):

        for name, val in var(cls).items():
            if callable(val):
                setattr(cls,name, wait_random()(val))

        return cls

    """
    Now you can wrap the entire class with @classwrapper. But what
if there are multiple scraper classes or multiple subclasses of the
scraper? You can either use @classwrapper on
them individually or in such a scenario, you can create a metaclass
    """
    class MyMetaClass(type):
        def __new__(cls, name, bases, attrs):
            for n, val in attrs.item():
                if callable(val):
                    setattr(cls, n, wait_random()(val))

    class SomeClass(Metaclasses = MyMetaClass):
        pass

    
        






    """
    You might have wondered why we use __new__ instead of
__init__ here. __new__ is actually the first
step in creating an instance. It is responsible for returning a new
instance of your class. __init__, on the other hand, doesnt
return anything. Its only responsible for initializing the instance after
its been created. A simple rule of thumb to remember: Use
new when you need to control the creation of a new instance;
use init when you need to control the initialization of a new
instance.

You wont often see __init__ being implemented in a metaclass
because its not that powerful. The class is already constructed
before __init__ is actually called. You can see it as having
a class decorator with the difference that __init__ would be
run when making subclasses, while class decorators are not called for
subclasses.
    """
    

    
