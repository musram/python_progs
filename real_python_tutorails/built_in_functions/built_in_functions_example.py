




if __name__ == "__main__":

    #The type() function either returns the type of the object or returns a new type object based on the arguments passed.

    #type(object) 


    numbers_list = [1, 2]
    print(type(numbers_list))

    numbers_dict = {1: 'one', 2: 'two'}
    print(type(numbers_dict))

    class Foo:
        a = 0

    foo = Foo()
    print(type(foo))

    #type(name, bases, dict)
    #name	a class name; becomes the __name__ attribute
    #bases	a tuple that itemizes the base class; becomes the __bases__ attribute
    #dict	a dictionary which is the namespace containing definitions for the class body; becomes the __dict__ attribute
    o1 = type('X', (object,), dict(a='Foo', b=12))

    print(type(o1))
    print(vars(o1))

    class test:
        a = 'Foo'
        b = 12
        
  
    o2 = type('Y', (test,), dict(a='Foo', b=12))
    print(type(o2))
    print(vars(o2))
    

    #The dir() method tries to return a list of valid attributes of the object. The dir() tries to return a list of valid attributes of the object. If the object has __dir__() method, the method will be called and must return the list of attributes.If the object doesn't have __dir__() method, this method tries to find information from the __dict__ attribute (if defined), and from type object. In this case, the list returned from dir() may not be complete. If object is not passed to the dir() method, it returns the list of names in the current local scope.

    number = [1, 2, 3]
    print(dir(number))

    print('\nReturn Value from empty dir()')
    print(dir())

    class Person:
        def __dir__(self):
            return ['age', 'name', 'salary']
    

    teacher = Person()
    print(dir(teacher))


    #The object() function returns a featureless object which is a base for all classes.

    obj = object()
    print(type(obj))
    print(dir(obj))




    #The vars() function returns the __dict__ attribute of the given object.
    #vars(object)

    #vars() returns the __dict__ attribute of the given object. If the object passed to vars() doesn't have the __dict__ attribute, it raises a TypeError exception. If no argument is passed to vars(), this function acts like locals() function.


    class Foo:
        def __init__(self, a = 5, b = 10):
            self.a = a
            self.b = b
  
    object = Foo()
    print(vars(object))


    #The globals() method returns the dictionary of the current global symbol table.
    print(globals())


    name= "sai"
    ocupation = "God"
    print(globals())

    print(globals()['name'])



    #A symbol table is a data structure maintained by a compiler which contains all necessary information about the program. These include variable names, methods, classes, etc. There are mainly two kinds of symbol table. Global symbol table and local symbol table. The global scope contains all functions, variables which are not associated to any class or function. Likewise, Local symbol table stores all information related to the local scope of the program, and is accessed in Python using locals() method. The local scope could be within a function, within a class, etc.


    #locals()

    print(locals())
    def localsNotPresent():
        return locals()

    def localsPresent():
        present = True
        return locals()

    print('localsNotPresent:', localsNotPresent())
    print('localsPresent:', localsPresent())    


    #The getattr() method returns the value of the named attribute of an object. If not found, it returns the default value provided to the function.

    #getattr(object, name[, default])

    class Person:
        age = 23
        name = "Adam"

    person = Person()

    # when default value is provided
    print('The sex is:', getattr(person, 'sex', 'Male'))

    # when no default value is provided
    #print('The sex is:', getattr(person, 'sex'))


    #The setattr() function sets the value of the attribute of an object.

    #setattr(object, name, value)
    class Person:
        name = 'Adam'
    
    p = Person()
    print('Before modification:', p.name)

    # setting name to 'John'
    setattr(p, 'name', 'John')

    print('After modification:', p.name)
    print(p.__dict__)


    # setting an attribute not present in Person
    setattr(p, 'age', 23)
    print('Age is:', p.age)
    print(p.__dict__)


    #The delattr() deletes an attribute from the object (if the object allows it).
    #delattr(object, name)

    delattr(p, 'age')
    print('after delattr', p.__dict__)

    #del p.age will also work


    

    #The hasattr() method returns true if an object has the given named attribute and false if it does not.
    #hasattr(object, name)

    print('Person has age?:', hasattr(person, 'age'))
    print('Person has salary?:', hasattr(person, 'salary'))


    #The hash() method returns the hash value of an object if it has one.
    #Hash values are just integers which are used to compare dictionary keys during a dictionary lookup quickly. Internally, hash() method calls __hash__() method of an object which are set by default for any object.

    #hash(object)

    print('hash of the Person object is ', hash(person))

    #But for correct hash implementation, __hash__() should always return an integer. And, both __eq__() and __hash__() methods have to be implemented.

    class Person:
        def __init__(self, age, name):
            self.age = age
            self.name = name

        def __eq__(self, other):
            return self.age == other.age and self.name == other.name

        def __hash__(self):
            print('The hash is:')
            return hash((self.age, self.name))

    person = Person(23, 'Adam')
    print(hash(person))



    #The id() function returns identity (unique integer) of an object.
    class Foo:
        b = 5
    dummyFoo = Foo()
    print('id of dummyFoo =',id(dummyFoo))

    var = 2
    print('id of var' , id(var))


    #The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument).

    #isinstance(object, classinfo)

    print(' isinstance of'+ str(isinstance(dummyFoo, Foo)))

    print('isinstance of' + str(isinstance(var, (int, tuple, float, Foo))))


    #he issubclass() function checks if the object argument (first argument) is a subclass of classinfo class (second argument).
    #issubclass(object, classinfo)

    
#class dict(**kwarg) class dict(mapping, **kwarg) class dict(iterable, **kwarg)    
