class spam:
    def __init__(self, name):
        self.name = name

    def bar(self):
        print( " iam in spam")

"""

class consists of data  together with functions that manipulate the data.
instance dict hold state and point to their class.
class dictionaries hold the functions

"""
What are it components?
(1) Name "spam"
(2) base class (Base,)
(3) FUnctions (__init__, bar)
"""

if __name__ == "__main__":
    
    """
    Step(1) 
    Body of class is isolated
    """
    def __init__(self, name):
        self.name = name
    
    def bar(self):
        print( " iam in spam")

    body = {'__init__':__init__, 'bar': bar}


    spam = type("spam", (object,), body)
    s = spam("Sai")
    print(s.__dict__)
    print(spam.__dict__)




    #metaclasses

    class mytype(type):
        def __new__(cls, name, bases, clsdict):
            if len(bases) > 1:
                raise TypeError("No")
            return super().__new__(cls, name, bases, clsdict)

    class Base(metaclass=mytype):
        pass

    class A(Base):
        pass

    class B(Base):
        pass

    try:
        class C(A,B):
            pass
    except TypeError as e:
        print(e)


    """
    Meta class gets the information about the  class defination at the time of definations

    (1) Can inspect this data
    (2) can modify this data

    Meta class  propagate down hierarchies
    class Base(metaclass=mytype)
    
    class spam(Base):  

    class grok(spam):

    """


    """
    Big picture
    decorators for function

    class decorators for class

    metaclass for class hierarchies
    """









    #class as a functions.

    class Funky:
        def __call__(self):
            print(f"Look at me, I work like a function")

    f = Funky()
    f()

    """
    https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/
    Class , instance.foobar
    (1)  call class.__getattribute__('foobar')
       (1.a) if hastattr(class.__dict__['foobar'], __get__) i.e is data descriptor.
       if yes?
          (1.a.a) return Class.__dict__['foobar'].__get__(instance, class)
       if no?
          (1.a.b) if hasattr(instance, 'foobar')?
                if yes?
                   return instance.__dict__['foobar']

    (1) return instane.__dict__['foobar'] 
    (2) 


    
    """

    """
    __new__ method is the constructor( it returns the new instance) while
    __init__ is initializer( the instance is already created when __init__ is called).


    you'd expect that __new__ would be looked up on the metaclass, but alas, it wouldn't be so useful that way so it's looked up statically
    """

    
    class Foobar:
        def __new__(cls):
            print(f" __new__ is executed")
            return super().__new__(cls)











    #build a generalized init methods

    class Structure:
        _fields = []
        def __init__(self, *args):
            if len(self._fields) != len(args):
                raise TypeError('Wrong #of argumentd')
            for name, val in zip(self._fields, args):
                setattr(self, name, val)
                  
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    class Point(Structure):
        _fields = ['x', 'y']

    s = Stock("ACEM", 100, 30.5)
    print(s.name)

    from  inspect import signature
    print(signature(Stock))

    sig = signature(

    def func(*args, **kwargs):
        bound_args = signature.bind(*args, **kwargs)
        for name, val in bound_args.arguments.items():
            print(name, "=", val)

    func(1,2,3)
        
    s = Stock(name="ACEM", shares=100, price=30.5)
    print(s.name)
        
    
        