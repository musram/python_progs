
class Foo:
    pass





if __name__ == "__main__":

    obj = Foo()
    print(type(Foo))    # the type of class is itself type
    print(obj.__class__)
    print(type(obj))     # the type of instance object obj is class Foo
    print(obj.__class__ is type(obj))

    n =  5
    print(type(n))
    print(n.__class__ is type(n))

    d = { 'x' : 1, 'y' : 2 }
    x = Foo()
    for obj in (n, d, x):
        print(type(obj) is obj.__class__)

    print('type of x is', type(x)) 
    print('type of Foo is', type(Foo))

    for t in int , float, dict, list, tuple:
        print(type(t))

    print(type(type))  #  type of type is type

    #type is a metaclass, of which classes are instances. Just as an ordinary object is an instance of a class, any new-style class in Python, and thus any class in Python 3, is an instance of the type metaclass.

    '''
       x is an instance of class Foo.
       Foo is an instance of the type metaclass.
       type is also an instance of the type metaclass, so it is an instance of itself.
    '''

    #type of built-in functions is the type of the object.
    print(type(1))
    print(type([1,2,3]))
    print(type((1,2,3)))
    class Foo:
        pass
    print(type(Foo()))

    '''
    You can also call type() with three argumentstype(<name>, <bases>, <dct>): 
<name> specifies the class name. This becomes the __name__ attribute of the class.
<bases> specifies a tuple of the base classes from which the class inherits. This becomes the __bases__ attribute of the class.
<dct> specifies a namespace dictionary containing definitions for the class body. This becomes the __dict__ attribute of the class.
Calling type() in this manner creates a new instance of the type metaclass. In other words, it dynamically creates a new class.
    '''




    #how classes work

    class point(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def move(self, dx, dy):
            self.x += dx
            self.y += dy



    #the above class is created as
    name = 'point'
    bases = (object,)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    methods = { '__init__':__init__, 'move':move}

    point = type(name, bases, methods)

    print(name)
    print(bases)
    print(methods)


    p = point(2,3)
    print(type(p))
    print(p.x)


    #example 1
    Foo = type('Foo', (), {})
    x = Foo()
    print(x)

    class Foo:
       pass

    y = Foo()
    print(y)

    #Example 2
    Bar = type('Bar', (Foo,), dict(attr=100))
    x = Bar()
    print(x.attr)
    print(x.__class__)
    print(dir(x))
    print(x.__class__.__bases__)


    #Example 3
    Foo = type('Foo', (), { 'attr':100, 'attr_val': lambda x : x.attr})
    x = Foo()
    print(x.attr)
    print(x.attr_val())

    class Foo:
        attr = 100
        def attr_val(self):
            return self.attr
    
    print(x.attr)
    print(x.attr_val())

    #example 4

    def f(obj):
        print('attr=', obj.attr)

    foo = type('foo', (), {'attr':100, 'attr_val':f})
    x = foo()
    print(x.attr)
    print(x.attr_val())

    class Foo:
        attr = 100
        attr_val = f

    print(x.attr)
    print(x.attr_val())



    


    #custom metaclass

    #In the same way that a class functions as a template for the creation of objects, a metaclass functions as a template for the creation of classes. Metaclasses are sometimes referred to as class factories.

    class Meta(type):
        def __new__(cls, name, bases, dct):
            print(cls)
            print(name)
            print(bases)
            x = super().__new__(cls, name, bases,  dct)
            x.attr = 100
            return x

    class Foo(metaclass = Meta):
        pass

    # This is same as
    Foo = Meta(name, bases, methods)
    
    print(Foo.attr)

    class Bar(metaclass = Meta):
        pass
    print(Bar.attr)


    #diamond not allowed in subclassing

    '''

    class Meta1(type):
        pass

    class Meta2(type):
        pass

    class Base1(metaclass=Meta1):
        pass

    class Base2(metaclass=Meta2):
        pass

    class Foobar(Base1, Base2):
        pass

    '''

    class Meta(type):
       pass

    class SubMeta(Meta):
       pass

    class Base1(metaclass=Meta):
        pass

    class Base2(metaclass=SubMeta):
        pass

    class Foobar(Base1, Base2):
        pass
    
    #object Factory

    class Foo:
        def __init__(self):
            self.attr = 100

    x = Foo()
    print(x.attr)

    y = Foo()
    print(y.attr)

    z = Foo()
    print(z.attr)

    #class factory

    class Meta(type):
        def __init__(cls, name, bases, dct):
            cls.attr = 100

    class X(metaclass = Meta):
        pass

    print(X.attr)

    class Y(metaclass = Meta):
        pass

    print(Y.attr)


    class Z(metaclass = Meta):
        pass

    print(Z.attr)


    #simple inheritace

    class Base:
        attr =  100

    class X(Base):
        pass

    class Y(Base):
        pass

    print(X.attr)
    print(Y.attr)

    #class decorator

    def decorator(cls):
        class NewClass(cls):
            attr = 100
        return NewClass

    @decorator
    class X:
        pass

    @decorator
    class Y:
        pass

    print(X.attr)
    print(y.attr)


    #some more examples

    class Dog:
        def __new__(cls, *args, **kwargs):
            print(cls)
            return super().__new__(cls, *args, **kwargs)

    dog = Dog()
    print(dog)

    dog_class = dog.__class__
    print(dog_class)

    print(dog_class.__class__)



    #one example
    import pprint

    class PrettyPrinterWrapper(type):
        def __new__(cls, name, bases, dict):
            """ define a new handler attribute a pretty printer instance """
            dict['pp'] = pprint.PrettyPrinter(width=20)

            return super().__new__(cls, name, bases, dict)

    class A(metaclass=PrettyPrinterWrapper):
        def __init__(self, my_list):
            self.list = my_list

        def __str__(self):
            return self.pp.pformat(self.list)

    a = A(["one", "two", "three"])

    print(a)


