#simple decorator

def my_decorator(func):
    def wrapper():
            print("something is happening before the function is called")
            func()
            print("something is happening after the function is called")
    return wrapper

def say_whee():
    print("Wee!")


#using @

def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

@do_twice
def say_dhee():
    print("dhee!")


#decorating functions with argument    
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print('hello {}'.format(name))

# Returning values from decorated functions


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("creating greeting")
    return  'hi {}'.format(name)

#to save the information about the decorated function
import functools
def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def say_hee():
    print("He man")


# Boiler plate template for the building complex decorators
def decortor(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        #Do somthinge before
        value = func(*args, **kwargs)
        #Do something after
        return value
    return wrapper_decorator



#  usecases of decorators

# timer

import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print('Finshed {!r} in {} secs'.format(func.__name__, run_time))
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(1000)])

              
# logger

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = ["{}={!r}".format(k,v) for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print("Calling {!r}({!r})".format(func.__name__, signature))
        value = func(*args, **kwargs)
        print("{!r} returned {!r}".format(func.__name__, value))           # 4
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return "Howdy {}!".format(name)
    else:
        return "Whoa {}! {} already, you are growing up!".format(name, age)



#slow down
def slow_down(func):
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down



@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


# built in decorators
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535



#using the created decorators on the class
class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])

#class decorators same as TimeWaster = timer(TimeWaster)
@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])




# multiple decorator

@debug
@do_twice
def greet(name):
    print('{}'.format(name))


#decorators with arguments

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_decorator_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_decorator_repeat
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print("Hello {}".format(name))

#or use this

repeating = repeat(num_times=4)

@repeating
def greet(name):
    print("Hello {}".format(name))



# decorators with and without arguments

def repeat(_func=None, *, num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_decorator_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_decorator_repeat
    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)

#@repeat
#def say_whee():
#    print("Whee!")    

@repeat(num_times=4)
def greet(name):
    print("Hello {}".format(name))


# stateful decorators
def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print("Call {} of {!r}".format(wrapper_count_calls.num_calls,func.__name__ ))
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

@count_calls
def say_whee():
    print("Whee!")



#class decorators


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print("Call {} of {!r}".format(self.num_calls,self.func.__name__ ))
        return self.func(*args, **kwargs)

@CountCalls
def say_whee():
    print("Whee!")



#decorating a class


def typed_property(name, expected_type):
    private_name = '_' + name


    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError("Expected {}".format(expected_type))
        setattr(self, private_name, value)

    return prop

Integer = lambda name: typed_property(name, int)
Float = lambda name: typed_property(name, float)
String = lambda name: typed_property(name, str)



def validate(**kwargs) :
    def decorate(cls):
        for name, val in kwargs.items():
            setattr(cls, name, val(name))
        return cls
    return decorate

@validate(name=String, shares=Integer, price = Float)
class Holding:
    def __init__(self, name, date, shares, price):
        self.name = name;
        self.data = date;
        self.shares = shares;
        self.price = price;







    
        
if __name__ == "__main__":
    say_whee = my_decorator(say_whee)
    print(say_whee)
    say_whee()

    #using @
    say_dhee()

    #usind with arguments
    greet("sai")


    #returning arguments
    hi_adams = return_greeting("Adams")
    print(hi_adams)

    #decorated function information lost
    say_dhee.__name__

    help(say_dhee)

    
    #decorated function with functools.wraps
    say_hee()
    say_hee.__name__

    help(say_hee)

    
    #usecases of the complex decorators
    waste_some_time(1)

    waste_some_time(999)


    make_greeting("Benjamin")

    make_greeting("richard", age=112)

    countdown(3)

    
    #built in decorators
    c = Circle(5)
    print(c.radius)
    print(c.area)

    c.radius = 10
    print(c.radius)
    print(c.area)


    #cant do c.area = 100

    c = Circle.unit_circle()
    print(c.radius)

    print(c.pi())

    print(Circle.pi())


    #using the created decorators on the class
    tw = TimeWaster(10)

    tw.waste_time(999)
    
    

    #multiple decorators
    greet("eva")

    #decorators with arguments
    greet("world")

    # decorators with and without arguments

    #say_whee()

    #greet("Penney")

    #stateful  decorators

    say_whee()

    say_whee()

    #say_whee.num_calls

    #class decorators

    say_whee()

    say_whee()

    #say_whee.num_calls

    #decorating a class

    h = Holding('AA', '2007-06-11', 100, 32.2)
    h.shares = '100'
    
    
    
