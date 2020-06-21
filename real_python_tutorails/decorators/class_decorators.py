#https://krzysztofzuraw.com/blog/2016/python-class-decorators.html





if __name__ == "__main__":

    class decorator:
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            print(f"called {self.func.__name__} with {args} and {kwargs}")
            return self.func(*args, **kwargs)
       


    @decorator
    def func(x,y):
        return x,y



    func(1,2)


    #But there is another special method that can be used in such cases: __get__. This is used for example in implementation of cached_property decorator in django.

    
    class property_:
        def __init__(self, func):
            self.func = func

        def __get__(self, instance, cls):
            print(f"called property from {instance} of class {cls}")
            return self.func(instance)


        def __set__(self, obj, value):
            print(f"setting up {value} for {obj}")
            [setattr(obj, k, v) for k,v in value.items()]

    class Apple(object):

        @property_
        def get_color(self):
            print('Accessing get_color property')
            return 'red'


    apple = Apple()
    print(apple.get_color)
    apple.get_color = {'shape':'triangle'}
    print(apple.shape)



    #You can also decorate classes and functions at the same time.

    from functools import wraps
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"called {args} and {kwargs}")

        return wrapper


    @decorator
    def add(a,b):
        return a+b


    class C:
        @decorator
        def method(self, a,b):
            print(a,b)


    add(1,2)
    c = C()
    c.method(3,4)



   #decorate whole classes,

    def decorator(cls):
        class Wrapper(object):
            def __init__(self, *args):
                self.wrapped = cls(*args)

            def __getattr__(self, name):
                print('Getting the {} of {}'.format(name, self.wrapped))
                return getattr(self.wrapped, name)

        return Wrapper

    @decorator
    class C(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

    x = C(1,2)
    print(x.x)        
            
    
