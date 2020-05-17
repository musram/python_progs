class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


class MyClassFunnyNames:
    def method(the_object):
        return 'instance method called', the_object

    @classmethod
    def classmethod(the_class):
        return 'class method called', the_class

    @staticmethod
    def staticmethod():
        return 'static method called'

    



if __name__ == "__main__":
    obj = MyClass()
    print(obj.method())

    print(MyClass.method(obj))


    print(MyClass.classmethod())

    print(MyClass.staticmethod())

    obj_funny = MyClassFunnyNames()
    print(obj_funny.method())

    print(MyClass.method(obj_funny))


    print(MyClass.classmethod())

    print(MyClass.staticmethod())
