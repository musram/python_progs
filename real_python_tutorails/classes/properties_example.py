class Holding:
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, newprice):
        if not isinstance(newprice, float):
            raise TypeError('Expected float')

        if newprice < 0:
            raise ValueError('Must be >= 0')
        
        self._price = newprice


    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, newshares):
        if not isinstance(newshares, int):
            raise TypeError('Expected int')

        self._shares = newshares
    


    #methods can also be decorated with property    
    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


    def __repr__(self):
        return 'Holding({!r},{!r},{!r},{!r}'.format(self.name, self.date, self.shares,  self.price)


    def __str__(self):
        return '{} shares of {} at ${:0.2f}'.format(self.shares, self.name, self.price)




# how to use @property  for all the  attributes

class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Expected integer")
        instance.__dict__[self.name] = value


        
class Float:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise TypeError("Expected flaot")
        instance.__dict__[self.name] = value


class Holding2:
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    #methods can also be decorated with property    
    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


    def __repr__(self):
        return 'Holding({!r},{!r},{!r},{!r}'.format(self.name, self.date, self.shares,  self.price)


    def __str__(self):
        return '{} shares of {} at ${:0.2f}'.format(self.shares, self.name, self.price)

        

#the above class Interger and Float can furthur made compact

class Typed:
    expected_type = object
    def __init__(self, name):
        self.name = name

    def __get__(self, instance):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError("Expected{}".format(self.expected_type))
        instance.__dict__[self.name] = value

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
    

    

if __name__ == "__main__":
    h = Holding("AA", "2007-12-2", 100, 34.4)

    try:
        h.price = "sai"
    except  TypeError as e:
        print(e)

    h.price  = 100.0

    print(h.__dict__)


    print(h.cost)


    #how does property method works?

    print(h.__class__)

    print(h.__class__.__dict__)

    print(h.__class__.__dict__['shares'])

    #when we call h.shares, these things happens iternally in python

    p = h.__class__.__dict__['shares']

    print(p)



    print(hasattr(p, '__get__'))

    print(p.__get__(h))

    #When we call h.shares = 200 , these this  internally happens in python

    p = h.__class__.__dict__['shares']

    print(hasattr(p, '__set__'))

    try:
        print(p.__set__(h, 100.0))
    except TypeError as e:
        print(e)



    h = Holding2("AA", "2007-12-3", 100, 34.4)

    print(h.shares)

    try:
        h.shares = 100.0
    except TypeError as e:
        print(e)
    
