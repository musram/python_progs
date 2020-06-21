#attribute access

"""
attribute access
(1) instance dict
(2) class dict
(3) mro dict


attribute set
(1) instance dict


both attribute access and attribute set used dict in hirarchy

so need to have method as hassattr, setattr and getattr which does that search in dict


dunder method __getattr__ is called when attribute is not found

"""



#examples


class Foo:
    integer = 1
    my_list = []
    foo = lambda x: x


class Bar(Foo):
    subfield = "sub"


class InfiniAttr:
    def __getattr__(self, name):
        setattr(self, name, InfiniAttr())
        return getattr(self,name)


class Immutable:
    def __init__(self, x):
        self.x = x

    def __setattr__(self, name, value):
        raise AttributeError(f"cannot set {name}, {type(self).__name__} is immutable")
       

class Immutable1:
    def __init__(self, x):
        self.x = x

    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError(f"cannot set {name}, {type(self).__name__} is immutable")
        else:
            setattr(self, name, value)

class Immutable2:
    def __init__(self, x):
        self.x = x

    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError(f"cannot set {name}, {type(self).__name__} is immutable")
        else:
            self.__dict__[name]= value

# How about the mehods?

class Person:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

        

class BindMe:
    def __get__(self, obj, type=None):
        print(f"binding {self} to {obj} , {type=}")
        return "Hello Descriptors"

class Test:
    x  = BindMe()


#example of bind method

class ClsWithStatic:
    @staticmethod
    def foo(a,b):
        return a+b

#implement this with decorators

from functools import wraps
def naive_static(func):
    @wraps(func)
    def wrapper(self,*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
    
    
    
class ClsWithStatic1:

    @naive_static
    def foo(a,b):
        return a+b

class good_static:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, type=None):
        return self.func

class ClsWithStatic2:

    @naive_static
    def foo(a,b):
        return a+b

    @good_static
    def bar(a,b):
        return a+b



class setter:
    def __set__(self, obj, value):
        print(f'setting {self} on {obj} to {value}')
        obj.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name
        
class TestSetter:
    x = setter()

    def __init__(self, x):
        self.x  = x




class TypeChecked:
    def __init__(self, type, optional=False):
        self.type = type

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, obj, value):
        if not isinstance(value , self.type):
            raise TypeError(f"{self.name} must be of type {self.type}")
        obj.__dict__[self.name] = value

class DescriptionPerson:
    name = TypeChecked(str)
    age = TypeChecked(int)
        

if __name__ == "__main__":

    print(Foo.__dict__)


    f1 = Foo()
    f2 = Foo()
    print(f1.__dict__)
    
    #attribute access

    #prints class integer
    print(Foo.integer)
    print(Foo.my_list)
    print(Foo.foo(2))

    
    # since integer in instaance dict is not there so prints from class dict
    print(f1.integer)
    print(f2.integer)


    #attribute set

    f1.integer = 4
    print(f1.integer)   #will print interger from instance dict rather than from class dict
    print(f2.integer)   #instance dict does not have integer so prints class dict integer
    print(Foo.integer)  #print class variable
    print(f1.__dict__)
    print(f2.__dict__)

    f1.my_list.append(2)

    #prints from class dict as instance dict does not have my_list
    print(f1.my_list)
    print(f2.my_list)
    print(Foo.my_list)


    f1.my_list = [3]   #set attribute my_list in instance dict of f1
    print(f1.my_list)  #access attribute my_list from f1 dict
    print(f2.my_list)  # access attribute my_list from class dict since f2 dict does note contain it
    print(Foo.my_list) #access class attribute my_list


    b = Bar()
    print(b.__dict__)
    print(Bar.__dict__)
    print(Bar.__base__.__dict__)

    #access attribute
    print(b.integer)  #access in instance b dict, then in Bar dict , then in Foo dict.

    b.z = 1
    print(b.__dict__)

    print(b.z)  #access in instance b dict.


    print(hasattr(f1, 'z'))
    print(hasattr(b, 'z'))
    print(getattr(b, 'z'))
    print(getattr(f1, "integer"))  # gets integer from f1 dict
    print(getattr(f2, "integer"))  #gets integer from Foo dict as f2 dict does not have "integer"

    setattr(f2, 'x', 100)
    print(getattr(f2, 'x'))


    foo = InfiniAttr()
    print(foo)
    print(foo.a)
    print(foo.__dict__)
    print(foo.a.a)
    print(foo.__dict__)

    try:
        im = Immutable(3)
    except AttributeError as e:
        print(e)


    try:
        im = Immutable1(3)
    except RecursionError as e:
        print(e)


    im = Immutable2(3)

    try:
        im.x = 2
    except AttributeError as e:
        print(e)
    im.z = 3
    print(im.__dict__)

    #method binding
    """
    -looking up .talk
        . on person.__dict__
        . on type(person).__dict__

    -get value in the __dict__
        . lambda function
        .  without referenc to person
    - but then
        . that function turns into
            . a bound method
            . with a reference to p
            . as self

    For objects the machinhery is in 
    object.__getattribute__() which transforms b.x into
    type(b).__dict__['x'].__get__(b, type(b))
    """

    
    person = Person(name="Max", age=108)
    print(person.__dict__)
    person.talk = lambda self: print(f' I am {self.name}')
    person.talk(person)


    Person.talk = lambda self:print(f' I am big than {self.name}')

    print(person.__dict__)

    print(Person.__dict__)

    person.talk(person)
    print(person.talk)
    Person.talk(person)
    print(Person.talk)




    t = Test()
    t.x

    Test.x


    #example of binding

    c  = ClsWithStatic()
    print(c.foo(1,2))

    print(ClsWithStatic.foo(1,2))


    c = ClsWithStatic1()
    print(c.foo(1,2))
    try:
        print(ClsWithStatic1.foo(1,2))
    except TypeError as e:
        print(e)

    c = ClsWithStatic2()
    print(c.foo(1,2))
    try:
        print(ClsWithStatic2.bar(1,2))
    except TypeError as e:
        print(e)


    t = TestSetter(3)

    print(t.x)

    t.x = 4
    print(t.x)

    print(TestSetter.x)



    p = DescriptionPerson()
    p.name = "sai"
    p.age = 0

    try:
        p.age = "0"
    except TypeError as e:
        print(e)
    

    
    

    
    

    
        


