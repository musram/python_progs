#The difference between getattr, __get__, __getattr__, and __getattribute__ in Python



class Foo:

    def __init__(self, name):
        self.name = name


class Frob:
    def __init__(self, bamf):
        self.bamf = bamf

    def __getattr__(self, name):
        print('Frob does not have {self.name} attribute')
        return object.__getattribute__(self, name)


class Drob(object):
    def __getattribute__(self, name):
        print( f'getting {name}')
        return object.__getattribute__(self, name)
       

class Descriptor(object):

    def __set_name__(self, owner,  name):
        self.name = name
        
    def __get__(self, obj, type):
        val  = obj.__dict__.get(self.name) or 0
        print(f'get value={val}') 
        return val
 
    def __set__(self, obj, val):
        
        print(f'set value={val}')
        obj.__dict__[self.name] = val

class Stu(object):
    age = Descriptor()




if __name__ == "__main__":

    f = Foo("sai")

    print(f.name)

    #getattr

    print(getattr(f, 'name'))

    print(getattr(f, 'x', 'bar'))  #if 'x' is not in f then default value 'bar' is returned



    #__getattr__


    f = Frob("bamf")
    print(f.bamf)

    try:
        print(f.foo)
    except AttributeError as e:
        print(e)


    # __ getarribute__

    d = Drob()
    try:
        print(d.bamf)
    except AttributeError as e:
        print(e)
    

    d.bamf = 10
    print(d.bamf)


    #__get__

    
    stu = Stu()
    stu.age = 12    # set value=12
    print(stu.age)

    print(stu.__dict__)
