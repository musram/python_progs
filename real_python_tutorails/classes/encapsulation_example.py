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


    def __repr__(self):
        return 'Holding({!r},{!r},{!r},{!r}'.format(self.name, self.date, self.shares,  self.price)


    def __str__(self):
        return '{} shares of {} at ${:0.2f}'.format(self.shares, self.name, self.price)



if __name__ == "__main__":
    h = Holding("AA", "2007-12-2", 100, 34.4)

    print(repr(h))
    print(str(h))


    print(h.__dict__)    # class variables are in __dict__

    h.yow = "hold"

    print(h.__dict__)

    del h.yow

    print(h.__dict__)


    print(h.__class__)

    print(Holding.__dict__)   # class methods are part of ClassName.__dict__

    print(Holding.__dict__['cost'])

    try:

        print(Holding.__dict__['cost']())
    except TypeError as e:
        print(e)

    print(Holding.__dict__['cost'](h))
