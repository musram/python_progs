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

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise TypeError("Expected flaot")
        instance.__dict__[self.name] = value


class Holding:
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
    """
    def __setattr__(self, name, value):
        if name not in {'name', 'shares',  'price', 'date'}:
            raise AttributeError('No attribute {}'.format(name))
        super().__setattr__(name, value)
    """
class spam:

    #called for all the attributes i.e missing and not missing
    def __getattribute__(self, name):

        return 'getting {}'.format(name)

class spam2:

    # only callad on missing attribute
    def __getattr__(self, name):
        return 'getting {}'.format(name)


#better examples of __getattr__ and __getattribute__


"""
Python will call __getattr__ method whenever you request an attribute that hasn't already been defined.
"""

class Count():
    def __init__(self,mymin,mymax):
        self.mymin=mymin
        self.mymax=mymax


class Count2:
    def __init__(self,mymin,mymax):
        self.mymin=mymin
        self.mymax=mymax    

    def __getattr__(self, item):
        self.__dict__[item]=0
        return 0


"""
Now lets see the __getattribute__ method. If you have __getattribute__ method in your class, python invokes this method for every attribute regardless whether it exists or not. So why we need __getattribute__ method? One good reason is that you can prevent access to attributes and make them more secure as shown in the following example.

Important: In order to avoid infinite recursion in __getattribute__ method, its implementation should always call the base class method with the same name to access any attributes it needs. For example: object.__getattribute__(self, name) or super().__getattribute__(item) and not self.__dict__[item]

"""

class Count3:

    def __init__(self,mymin,mymax):
        self.mymin=mymin
        self.mymax=mymax
        self.current=None

    def __getattribute__(self, item):
        if item.startswith('cur'):
            raise AttributeError
        return object.__getattribute__(self,item) 
        # or you can use ---return super().__getattribute__(item)



"""
If your class contain both getattr and getattribute magic methods then __getattribute__ is called first. But if __getattribute__ raises AttributeError exception then the exception will be ignored and __getattr__ method will be invoked. See the following example:
"""

class Count4(object):

    def __init__(self,mymin,mymax):
        self.mymin=mymin
        self.mymax=mymax
        self.current=None

    def __getattr__(self, item):
            self.__dict__[item]=0
            return 0

    def __getattribute__(self, item):
        if item.startswith('cur'):
            raise AttributeError
        return object.__getattribute__(self,item)
        # or you can use ---return super().__getattribute__(item)
        # note this class subclass object


if __name__ == "__main__":
    h = Holding("AA", "2007-12-3", 100,  32.2)

    #Methods to access. 

    #(1)
    print(h.shares)
    print(h.price)
    print(h.name)

    #(2)
    print(h.__dict__['shares'])
    
    #(3)
    print(getattr(h, 'name'))


    #(4)
    print(h.__getattribute__('name'))

    #The (4) method 


    try:

        print(h.__getattribute__('names'))
    except AttributeError as e:
        print(e)


    s = spam()
    s.x = 2
    s.y = 3
    print(s.x)
    print(s.y)
    print(s.joy)
    print(s.koy)

    try:
        print(getattr(h, 'names'))
    except AttributeError as e:
        print(e)

    s = spam2()

    s.x = 2
    s.y = 3

    print(s.x)
    print(s.y)

    print(s.joy)
    print(s.koy)


    #methods to set

    #(1)
    h.shares = 1000
    print(h.shares)

    #(2)
    h.__dict__['shares'] = 2000
    print(h.shares)


    #(3)
    setattr(h, 'shares', 3000)
    print(h.shares)


    #(4)

    h.__setattr__('shares', 100)
    print(h.shares)



    #methods to delete


    h.you = "sai"
    print(h.you)

    del h.you

    try:

        print(h.you)
    except AttributeError as e:
        print(e)

    h.you = "sai"
    print(h.you)

    h.__delattr__('you')

    
    try:

        print(h.you)
    except AttributeError as e:
        print(e)


    obj1 = Count(1,10)
    print(obj1.mymin)
    print(obj1.mymax)
    try:

        print(obj1.mycurrent)
    except AttributeError as e:
        print(e)


    obj1 = Count2(1,10)
    print(obj1.mymin)
    print(obj1.mymax)
    print(obj1.mycurrent1)

    print(obj1.__dict__)


    obj1 = Count3(1,10)
    print(obj1.mymin)
    print(obj1.mymax)

    try:

        print(obj1.current)        
    except AttributeError as e:
        print(e)



    obj1 = Count4(1,10)
    print(obj1.mymin)
    print(obj1.mymax)
    print(obj1.current)
    


  

    
    
