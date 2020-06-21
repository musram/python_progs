

"""
__new__ is called first. 
Class method 
   .takes in cls
makes self
   .returns it
takes same params as __init__
inherited from object



__init__ method is non-static method
   . takes in self
populates fields
void
inherited from object


__call__ is non-static method
  . takes in self
allows instances to be callable like functions
optional
  . not inherited from object
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        return self.name




if __name__ == "__main__":
    a = Person("sai", 0)
    print(a.talk())

    print(type(a))



    #construct the similar class with the types

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        return self.name
    

    alt_person = type( "alt_person", (object,), {'__init__': __init__, 'talk': talk, })

    b = alt_person("leah", 1)
    print(b.talk())
    print(type(b))

    
    #use of metaclasses

    class Person:
        def __init__(self, first, last):
            self.name = f'{first} {last}'

        def talk(self):
            print("I am", self.name)

        @classmethod
        def make_family(cls, fam_name):

            def __init__(self, first, last= fam_name):
                cls.__init__(self, first, last)
                return type('last_name', (cls, ), {'__init__': __init__})

    steve = Person('steve', 'job')
    steve.talk()

    fam = Person.make_family("patel")
    #print(fam)
    #me = fam("Sai")
    #print(me.talk())


    #type() is not a function. its a class.

    print(type(42))
    print(type(str))
    print(type(type))
    print(isinstance(type, type))
    print(type.__mro__)

    print(isinstance(type, object))
    print(isinstance(object, type))

    print(isinstance(1, object))
    print(isinstance(1,  type))


    class MetaClass(type):
        def __new__(meta, name, bases, attrs):
            print(f"__new__({meta}, {name}, {bases}, {attrs})")
            return type.__new__(meta, name, bases, attrs)

        def __init__(cls, name, bases, attrs):
            print(f"__new__({cls}, {name}, {bases}, {attrs})")
            return type.__init__(cls, name, bases, attrs)
        def __call__(cls, *args, **kwargs):
            print(f"__new__({cls}, {args}, {kwargs})")
            return type.__call__(cls, *args, **kwargs)


    def  __init__(self, name):
            self.name = name

    def talk(self):
            print(f'I am {self.name}')

    attrs = {'__init__': __init__ , 'talk': talk}
                  
    MetaPerson = MetaClass('MetaPerson', (object,), attrs)

    mp = MetaPerson("sai")
    mp.talk()
            
            
    
