#https://realpython.com/python-descriptors/
#https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/
#https://www.youtube.com/watch?v=bKR8CmfJdlI




"""
A descriptor is an object with any of the following methods (__get__, __set__, or __delete__), intended to be used via dotted-lookup as if it were a typical attribute of an instance. For an owner-object, obj_instance, with a descriptor object:

obj_instance.descriptor invokes
descriptor.__get__(self, obj_instance, owner_class) returning a value
This is how all methods and the get on a property work.

obj_instance.descriptor = value invokes
descriptor.__set__(self, obj_instance, value) returning None
This is how the setter on a property works.

del obj_instance.descriptor invokes
descriptor.__delete__(self, obj_instance) returning None
This is how the deleter on a property works.

obj_instance is the instance whose class contains the descriptor object's instance. self is the instance of the descriptor (probably just one for the class of the obj_instance)

"""





class Verbose_attribute():
    def __get__(self, obj, type=None) -> object:
        print("accessing the attribute to get the value")
        return 42
    def __set__(self, obj, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

class Foo():
    attribute1 = Verbose_attribute()

# Descriptors can be implemented via property

class Foo1():
    @property
    def attribute1(self) -> object:
        print("accessing the attribute to get the value")
        return 42

    @attribute1.setter
    def attribute1(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

#property(fget=None, fset=None, fdel=None, doc=None) -> object
"""
property() returns a property object that implements the descriptor protocol. It uses the parameters fget, fset and fdel for the actual implementation of the three methods of the protocol.
"""




# The above is same as below

class Foo2():
    def getter(self) -> object:
        print("accessing the attribute to get the value")
        return 42

    def setter(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

    attribute1 = property(getter, setter)

#python descriptors in methods and functions








#How Attributes Are Accessed With the Lookup Chain


class Vehicle():
    can_fly = False
    number_of_weels = 0

class Car(Vehicle):
    number_of_weels = 4

    def __init__(self, color):
        self.color = color


 #How to Use Python Descriptors Properly

"""
__get__(self, obj, type=None) -> object
__set__(self, obj, value) -> None

When you implement the protocol, keep these things in mind:

self is the instance of the descriptor youre writing.
obj is the instance of the object your descriptor is attached to.
type is the type of the object the descriptor is attached to.
In .__set__(), you dont have the type variable, because you can only call .__set__() on the object. In contrast, you can call .__get__() on both the object and the class.

"""

"""
Another important thing to know is that Python descriptors are instantiated just once per class. That means that every single instance of a class containing a descriptor shares that descriptor instance.
"""

class OneDigitNumericValue():
    def __init__(self):
        self.value = 0
    def __get__(self, obj, type=None) -> object:
        return self.value
    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value = value

class Foo3():
    number = OneDigitNumericValue()

        
"""
So, how can you solve this problem? You might think that itd be a good idea to use a dictionary to save all the values of the descriptor for all the objects its attached to. This seems to be a good solution since .__get__() and .__set__() have the obj attribute, which is the instance of the object youre attached to. You could use this value as a key for the dictionary.
"""

class OneDigitNumericValue2():
    def __init__(self):
        self.value = {}
        
    def __get__(self, obj, type=None) -> object:
        try:
            return self.value[obj]
        except:
            return 0
    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value[obj] = value

class Foo4():
    number = OneDigitNumericValue2()


"""
Unfortunately, the downside here is that the descriptor is keeping a strong reference to the owner object. This means that if you destroy the object, then the memory is not released because the garbage collector keeps finding a reference to that object inside the descriptor.
The best solution here is to simply not store values in the descriptor itself, but to store them in the object that the descriptor is attached to.
"""

class OneDigitNumericValue3():
    def __init__(self, name):
        self.name = name
        
    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0
    
    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value
        

class Foo5():
    number = OneDigitNumericValue3("number")


# in python3.6 we can do

class OneDigitNumericValue4():
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value

class Foo6():
    number = OneDigitNumericValue()

    












#application











#DRY


class Values:
    def __init__(self):
        self._value1 = 0
        self._value2 = 0
        self._value3 = 0
        self._value4 = 0
        self._value5 = 0

    @property
    def value1(self):
        return self._value1

    @value1.setter
    def value1(self, value):
        self._value1 = value if value % 2 == 0 else 0

    @property
    def value2(self):
        return self._value2

    @value2.setter
    def value2(self, value):
        self._value2 = value if value % 2 == 0 else 0

    @property
    def value3(self):
        return self._value3

    @value3.setter
    def value3(self, value):
        self._value3 = value if value % 2 == 0 else 0

    @property
    def value4(self):
        return self._value4

    @value4.setter
    def value4(self, value):
        self._value4 = value if value % 2 == 0 else 0

    @property
    def value5(self):
        return self._value5

    @value5.setter
    def value5(self, value):
        self._value5 = value if value % 2 == 0 else 0


class Evennumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None):
        return obj.__dict__.get(self.name) or 0
            
    def __set__(self, obj, value):
        obj.__dict__[self.name] = (value if value % 2 == 0 else 0)

class Values1:
     value1 = Evennumber()
     value2 = Evennumber()
     value3 = Evennumber()
     value4 = Evennumber()
     value5 = Evennumber()

     
    
        
            


    



if __name__ == "__main__":
    my_foo_object = Foo()
    x = my_foo_object.attribute1      #  calls __get__
    print(x)


    try:
        my_foo_object.attribute1 = 1      # calls __set__
        print(my_foo_object.attribute1)
    except AttributeError as e:
        print(e)
    

    my_foo_object = Foo1()
    x = my_foo_object.attribute1
    print(x)

    my_foo_object = Foo2()
    x = my_foo_object.attribute1
    print(x)


    print(dir(x))

    def has_descriptor_attrs(obj):
        return set(['__get__', '__set__', '__delete__']).intersection(dir(obj))

    def is_descriptor(obj):
        """obj can be instance of descriptor or the descriptor class"""
        return bool(has_descriptor_attrs(obj))

    def has_data_descriptor_attrs(obj):
        return set(['__set__', '__delete__']) & set(dir(obj))

    def is_data_descriptor(obj):
        return bool(has_data_descriptor_attrs(obj))

    print(is_descriptor(x))
    print(is_data_descriptor(x))

    #We can see that classmethod and staticmethod are Non-Data-Descriptors:

    print(is_descriptor(classmethod))
    print(is_data_descriptor(classmethod))


    #Note that all functions are also Non-Data-Descriptors:

    def goo():
        pass

    print(is_descriptor(goo))
    print(is_data_descriptor(goo))


    #However, property is a Data-Descriptor:

    print(is_descriptor(property))
    print(is_data_descriptor(property))

    
    
    
    





    my_car = Car("red")
    print(my_car.__dict__)
    print(type(my_car).__dict__)  #same as Car.__dict__
    print(Car.__dict__)

    #these two are same
    print(my_car.color)
    print(my_car.__dict__['color'])

    #these two are same
    print(my_car.number_of_weels)
    print(type(my_car).__dict__['number_of_weels'])

    #these two are sames
    print(my_car.can_fly)
    print(type(my_car).__base__.__dict__['can_fly'])


    """
    So, what happens when you access the attribute of an object with dot notation? How does the interpreter know what you really need? Well, heres where a concept called the lookup chain comes in:

First, youll get the result returned from the __get__ method of the data descriptor named after the attribute youre looking for.

If that fails, then youll get the value of your objects __dict__ for the key named after the attribute youre looking for.

If that fails, then youll get the result returned from the __get__ method of the non-data descriptor named after the attribute youre looking for.

If that fails, then youll get the value of your object types __dict__ for the key named after the attribute youre looking for.

If that fails, then youll get the value of your object parent types __dict__ for the key named after the attribute youre looking for.

If that fails, then the previous step is repeated for all the parents types in the method resolution order of your object.

If everything else has failed, then youll get an AttributeError exception.
    """




    # #How to Use Python Descriptors Properly

    
    my_foo_object = Foo3()
    my_second_foo_object = Foo3()

    my_foo_object.number = 3
    print(my_foo_object.number)
    print(my_second_foo_object.number)

    my_third_foo_object = Foo3()
    print(my_third_foo_object.number)




    my_foo_object = Foo4()
    my_second_foo_object = Foo4()

    my_foo_object.number = 3
    print(my_foo_object.number)
    print(my_second_foo_object.number)

    my_third_foo_object = Foo4()
    print(my_third_foo_object.number)


    my_foo_object = Foo5()
    my_second_foo_object = Foo5()

    my_foo_object.number = 3
    print(my_foo_object.number)
    print(my_second_foo_object.number)

    my_third_foo_object = Foo5()
    print(my_third_foo_object.number)



    my_foo_object = Foo6()
    my_second_foo_object = Foo6()

    my_foo_object.number = 3
    print(my_foo_object.number)
    print(my_second_foo_object.number)

    my_third_foo_object = Foo6()
    print(my_third_foo_object.number)



















    #application









    #DRY
    my_values = Values()
    my_values.value1 = 1
    my_values.value2 = 4
    print(my_values.value1)
    print(my_values.value2)

    my_values = Values1()
    my_values.value1 = 1
    my_values.value2 = 4
    print(my_values.value1)
    print(my_values.value2)
    
