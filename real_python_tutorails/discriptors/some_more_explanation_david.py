



class Descriptors:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, type:None):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


    def __delete__(self, instance):
        del instance.__dict[self.name]


class Stock:
    _fields = ['name', 'shares', 'price']

    name = Descriptors('name')
    shares = Descriptors('shares')
    price = Descriptors('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price



class Type(Descriptors):
    ty = object
    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError(f"Expected {self.ty}")
        super().__set__(instance, value)


class Integer(Type):
    ty = int

class Float(Type):
    ty = float

class String(Type):
    ty = str


class Stock1:
    _fields = ['name', 'shares', 'price']

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

class Positive(Descriptors):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"Must be > 0")
        super().__set__(instance, value)        #this will call the class above this class in the __mro__ list.

class PositiveInteger(Integer, Positive):       #order of super class matters here 
    pass
class PositiveFloat(Float,  Positive):
    pass



class Stock2:
    _fields = ['name', 'shares', 'price']

    name = String('name')
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


 
#check size
class Sized(Descriptors):
    def __init__(self, *args, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args,**kwargs)

    def __set__(self, instance, value):
        if len(value) > self.maxlen:
            raise ValueError(f"Too big")
        super().__set__(instance, value)

class SizedString(String, Sized):
    pass

#checl pattern

import re
class Regex(Descriptors):
    def __init__(self, *args, pat, **kwargs):
        self.pat = re.compile(pat)
        super().__init__(*args,**kwargs)

    def __set__(self, instance, value):
        if not self.pat.match(value):
            raise ValueError(f"Invalid Sring")
        super().__set__(instance, value)

class SizedRegexString(Regex, SizedString):      # or (Regex, String, Sized)
    pass


class Stock3:
    _fields = ['name', 'shares', 'price']

    name = SizedRegexString('name', pat='[A-z]+$', maxlen = 8)
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price



if __name__ == "__main__":
    s = Stock3("ACME", 100, 32.0)
    print(s.shares)
    s.shares = 200
    print(s.shares)
    print(s.__dict__)

    

    try:
        s.shares = "sai"
    except TypeError as e:
        print(e)

    try:
        s.shares = -100
    except ValueError as e:
        print(e)
        

    print(PositiveInteger.__mro__)


    try:
        s.name = "AUGILLIOJOJOPJPOOPOP"
    except ValueError as e:
        print(e)

    try:
        s.name = "I_1_2P"
    except ValueError as e:
        print(e)
