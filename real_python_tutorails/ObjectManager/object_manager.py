class Borg:
    _namespace = {}

    def __init__(self):
        self.__dict__ = Borg._namespace



class Base:
    def __init__(self):
        print('Base')

class Borg:
    _namespace = {}
    def __init__(self, *args, **kwargs):
        self.__dict__ = Borg._namespace
        print('Borg')


class Borg2:
    _namespace = {}
    def _new__(cls, *args, **kwargs):
        print('Borg')
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._namespace
        return obj
    
class Testing(Borg, Base):
    pass

class Testing2(Base, Borg):
    pass

class Testing3(Base, Borg):
        
    def __init__(self, *args, **kwargs):
        super().__init__()

class Testing4(Base, Borg2):
    pass



if __name__ == "__main__":

    a = Borg()
    b = Borg()

    print(a._namespace)

    setattr(a, 'name', "sai")

    print(a._namespace)
    print(hasattr(a,'name'))


    Testing()

    print(Testing.__mro__)


    Testing2()

    print(Testing2.__mro__)


    #(1) solution:

    #use super()

    Testing3()

    print(Testing3.__mro__)


    #(2) solution:

    #use __new__

    Testing4()
