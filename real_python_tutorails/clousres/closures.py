
class Holding:
    def __init__(self, name, date, shares, price):
        self.name = name;
        self.data = date;
        self.shares = shares;
        self.price = price;

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, newPrice):
        if not isinstance(newPrice, float):
            raise TypeError("Expected float")
        self._price = newPrice

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, newShares):
        if not isinstance(newShares, int):
            raise TypeError("Expected float")
        self._shares = newShares





if __name__ == "__main__":
    h = Holding('AA', '2007-06-11', 100, 32.2)
    h.price = "sai"
