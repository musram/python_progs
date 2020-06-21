class DataDescripter:
    def __init__(self):
        self.value = 0

    def __get__(self, instance, type=None):
        print(f'data descripter __get__')
        return self.value

    def __set__(self, instance, value):
        print(f'data descripter __set__')
        self.value = value

    def __delete__(self, instance):
        print('f dont delete')



class A:
    attr = DataDescripter()


class NonDataDescripter:
    def __init__(self):
        self.value = 0

    def __get__(self, instance, type=None):
        print(f'data descripter __get__')
        return self.value

class B:
    attr = NonDataDescripter()


from weakref import WeakKeyDictionary


class DescriptorWeakKeyDictStorage:
    _hidden =  WeakKeyDictionary()

    def __init__(self, default=None):
        self.default = default

    def __get__(self, instance, type=None):
        return DescriptorWeakKeyDictStorage._hidden.get(instance, self.default)

    def __set__(self, instance ,  value):
        DescriptorWeakKeyDictStorage._hidden[instance] = value

class StoreInstance:
    attr = DescriptorWeakKeyDictStorage(10)




#__getattribute__

class Overridden:
    attr = DataDescripter()
    def __getattribute__(self, name):
        print("no way")

    
if __name__ == "__main__":
    a = A()
    print(a.attr)

    #accessing value
    
    #this is same as
    print(type(a).__dict__['attr'].__get__(a, type(a)))

    print(A.attr)

    #this is same as
    print(A.__dict__['attr'].__get__(None, A))

    print(A.__dict__)


    #setting value

    a.attr = 10          #will call the __set__ of DataDescripter
    print(a.attr)        #will call the __get__  of DataDescripter


    A.attr = 100         # this will call A.__dict__['attr'] 100 which is normal thing
    print(a.attr)
    print(A.attr)

    print(a.__dict__)
    print(A.__dict__)


    #NonDataDescripter

    b = B()

    print(b.attr)

    b.attr = 20        #since no __set__ methods, it will store in __dict__ of instance.
    print(b.attr)
    print(b.__dict__)


    o = Overridden()
    o.attr



    #


    s1 = StoreInstance()
    s2 = StoreInstance()

    print(s1.attr)
    print(s2.attr)

    
    
