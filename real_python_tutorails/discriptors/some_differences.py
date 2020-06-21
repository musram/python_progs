#The difference between getattr, __get__, __getattr__, __getattribute__  and __getitem__in Python



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


class Krob:
    def __init__(self):
        self.x = 10
    def __getattr__(self,name):
        print(f"__getattr__ called")
        return name
    def __getattribute__(self, name):
        print(f"__getattribute__ called")
        if name == 'bar':
            raise AttributeError
        return 'getattribute'
    
       

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


class MyColors:
    def __init__(self):
        self._colors = {'yellow': 1, 'red': 2, 'blue': 3}
    def __getitem__(self, name):
        return self._colors.get(name, 100)




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


    #diff between __getattr__ and __getattribute__

    k =  Krob()
    print(k.x)    #calls __getattribute__
    print(k.baz)  # calls __getattribute__
    print(k.bar)  # calls __getattribute__ but raising  AttributeError calls __getattr__
    
    


    #__get__

    
    stu = Stu()
    stu.age = 12    # set value=12
    print(stu.age)

    print(stu.__dict__)




    #__getitem__
    #Are methods that can be defined to implement container objects.


    colors = MyColors()
    print(colors['yellow'])
    print(colors['brown'])





    """

    getattr, setattr

    __getattr__, __getattribute__, __setattr__, __delattr__

    __get__, __set__, __del__

    __getitem__ , __setitem__, __delitem__

   """


    
