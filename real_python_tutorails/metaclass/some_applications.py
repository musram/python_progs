#https://breadcrumbscollector.tech/when-to-use-metaclasses-in-python-5-interesting-use-cases/

class MyMeta(type):
    def __new__(cls, name, base, namespace):
        return super().__new__(cls, name, base, namespace)

class MyClass(metaclass = MyMeta):
    x  = 3




if __name__ == "__main__":
    my_class = MyClass()
    print(my_class.__dict__)
    print(MyClass.__dict__)

    print(isinstance(MyClass, type))
    print(isinstance(MyClass, MyMeta))

    #Avoiding decorators repetition or decorating all subclasses

    def typed_property(name, expected_type):
        private_name = '_' + name


        @property
        def prop(self):
            return getattr(self, private_name)

        @prop.setter
        def prop(self, value):
            if not isinstance(value, expected_type):
                raise TypeError("Expected {}".format(expected_type))
            setattr(self, private_name, value)

            return prop


    Integer = lambda name: typed_property(name, int)
    Float = lambda name: typed_property(name, float)
    String = lambda name: typed_property(name, str)



    def validate(**kwargs) :
        def decorate(cls):
            for name, val in kwargs.items():
                setattr(cls, name, val(name))
                return cls
            return decorate

    @validate(name=String, shares=Integer, price = Float)
    class Holding:
        def __init__(self, name, shares, price):
            self.name = name;
            self.shares = shares;
            self.price = price;

                
    @validate(name=String, shares=Integer, price = Float)
    class Holding2:
        def __init__(self, name, shares, price):
            self.name = name;
            self.shares = shares;
            self.price = price;

    class MyMeta(type):
        def __new__(cls, name, bases, namespace):
            new_cls = super().__new__(cls, name, bases, namespace)
            return validate(name=String, shares=Integer, price=Float)(new_cls)

   
    class Holding(metaclass = MyClass):
        pass

    class Holding1(metaclass = MyClass):
        pass


    my_class = Holding()

                
    
    
