class Holding:
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


#classmethod

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, s):
        parts = s.split('-')
        return cls(int(parts[0]), int(parts[1]), int(parts[2]))

    @classmethod
    def today(cls):
        import time
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)



class MyDate(Date):
    def yow(self):
        print('yow')


"""
DIff between __init__ vs __new__.
__init__ is used to initialize the instance.self
   - sets up field
   - nonstatic
__new__ is used to create that instance in first place
   - static
   - takes in cls instead of self
   - if superclasses __new__ is called then __init__ will also be called.
"""

class Test:
    def __new__ (cls, x):
        print(f'__new__.cls={cls}')
        return super().__new__(cls)
    def __init__(self, x):
        print(f'__init__.self={self}')
        self.x  = x

        
    



if __name__ == "__main__":
    h = Holding('AA', '2006-13-12', 100, 34.3)

    #get method
    print(h.name)

    #set method
    h.shares = 200
    print(h.shares)

    #delete methos
    h.share = 300
    print(h.share)

    del h.share
    try:
        print(h.share)
    except AttributeError as e:
        print(e)

    print(h.cost)

    a = h.cost

    print(a())


    print(getattr(h, 'name'))   # same as h.name

    setattr(h, 'shares', 400)  #same as h.shares = 400
    print(h.shares)


    #ussage of getattr

    output_cols = ['name', 'shares', 'price']

    for col in output_cols:
        print(col, getattr(h, col))


    f = Date.today()
    print(f.year)
    print(f.month)


    e = Date.from_string('2000-12-01')
    print(e.year)
    print(e.month)


    g = MyDate.today()
    print(g.month)
    g.yow()


    t = Test(3)

    #every thing is object

    print(type(1))
    print(type(1).mro())
    print(type("hi").mro())
    print(type([]).mro())
    print(type(print).mro())
    
    

    

    
