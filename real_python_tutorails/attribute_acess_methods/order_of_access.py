"""
without descripters

(1) _getattribute__  if this generates AttributeError then goto (5)
(2) instance value
(3) Class defination
(4) Superclass recursively
(5) __getattr__
(6) AttributeError


with nondata descripters

(1) _getattribute__  if this generates AttributeError then goto (5)
(2) instance value
(3) Class defination       if there is descripters in class  with __get__ then                           return that.
(4) Superclass recursively if there is descripters in superclass  with __get__ then                           return that.
(5) __getattr__
(6) AttributeError

with data descripters
(1) _getattribute__  if this generates AttributeError then goto (5)
(1.5) Data descripters in class dict
(2) instance value
(3) Class defination       if there is descripters in class  with __get__ then                           return that.
(4) Superclass recursively if there is descripters in superclass  with __get__ then                           return that.
(5) __getattr__
(6) AttributeError

"""



if __name__ == "__main__":

    #Mixins
    
    class A:
        def a(self):
            print("you called a")
    class B:
        def b(self):
            print("you called b")

    class C:
        def c(self):
            print("you called c")

    import itertools

    for parents in itertools.combinations([A,B,C], 2):
        classname = ''.join([c.__name__ for c in parents])
        globals()[classname] = type(classname, parents, {})

    print(globals())
    print(AB.__bases__)
    ab = AB()
    print(ab.a())
    print(ab.b())
    try:
        print(ab.c())
    except AttributeError as e:
        print(e)



    #function as metaclass

    def stupid_metaclass(classname, bases, attrdict):
        return type(classname, bases, attrdict)

    class MyClass(metaclass = stupid_metaclass):
        pass

    print(type(MyClass))


    #class as metaclass

    class MyMeta(type):
        pass

    class MyClass(metaclass = MyMeta):
        pass

    instance = MyClass()



    """

    Normal inheritance
    
            instance
    type   <-------      object
                         
    |                      |
    |                    inherits
                           |
    instance of  -----    Car <-----instance of   ------ my_car

    """

    """
    Meta class
   
            instance
    type   <-------      object
                         
    |                      |
    |inherits from     inherits
                           |
    CarMeta<-instance of--Car <-----instance of   ------ my_car

    

    
