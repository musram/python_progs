#https://florian-dahlitz.de/blog/introduction-to-functools#singledispatch-function-overloading
import functools




"""Imagine, you have a large dataset and in order to analyse it, you implement a class holding the whole dataset. Furthermore, you implement functions to calculate information like the standard deviation of the dataset at hand. The problem: Each time you call the method, the standard deviation it calculated again - and this takes time! This is where @cached_property comes into play. Its purpose is to transform a method of a class into a property whose value is computed once and then cached as a normal attribute for the lifetime of the instance."""

class Dataset:
    def __init__(self, seq_of_numbers):
        self._data = seq_of_numbers

    @functools.cached_property
    def stdev(self):
        return statistics.stdev(self._data)

    @functools.cached_property
    def variance(self):
        return statistics.varaince(self._data)





if __name__ == "__main__":
    # dataset = Dataset([ i for i in range(1000)])
    # print(dataset.stdev())


    # reduce
    from operator import add, mul
    iterable = [ i for i in range(10)]

    result = functools.reduce(add, iterable)
    print(result)

    result = functools.reduce(mul, iterable)
    print(result)

    """The idea behind the update_wrapper() function is to update a wrapper function (as the name suggests) in a way that it looks like the wrapped function. In order to achieve this, update_wrapper() assigns the wrapped functions __module__, __name__, __qualname__, __annotations__, and __doc__ to the wrapper function ones. Furthermore, it updates the wrapper functions __dict__. Lets have a look at the @wraps decorator for a practical example."""

    
    def show_args(func):
        def wrapper(*args, **kwargs):
            print('calling function {} with {} and {}'.format(func.__name__, args, kwargs))
            return func(*args, **kwargs)

        return wrapper



    @show_args
    def add(a,b):
        """ Add two numbers a and b and return the result """
        return a+b

    print(add(2,3))
    print(add.__doc__)
    print(add.__name__)

    """Did you expect to see a different documentation string and name than the ones printed? This is because we did not access the wrapped functions documentation string and name but the ones from the wrapper function. This is were @wraps comes into play. The only thing we need to change in our code is to apply the decorator to the wrapper() function."""


    def show_args(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('calling function {} with {} and {}'.format(func.__name__, args, kwargs))
            return func(*args, **kwargs)

        return wrapper

    @show_args
    def add1(a,b):
        """ Add two numbers a and b and return the result """
        return a+b
    

    print(add1(2,3))
    print(add1.__doc__)
    print(add1.__name__)



    #@total_ordering
    """ 
    Programming in Python often involves writing your own classes. In some cases, you want to be able to compare different instances of that class. Depending on how you want to compare them, you might end up by implementing functions like __lt__(), __le__(), __gt__(), __ge__() or __eq__() to be able to use the corresponding <, <=, >, >=, and == operators. On the other hand, you could utilize the @total_ordering decorator. This way, you only need to implement one or more rich comparison ordering methods and the decorator supplies the rest. Additionally, it is recommended to define the __eq__() method, too.

Lets suppose you have a class Pythonista and you want to be able to order them lexicographically. To be able to do that, you need to implement the rich comparison ordering methods. But instead of implementing all of them, we only implement the __lt__() method as well as the __eq__() method. By using the @total_ordering decorator, the other ones are automatically defined.
"""

    from functools import total_ordering

    @total_ordering
    class Pythonista:
        firstName: str
        secondName: str

        def __init__(self, firstName: str, secondName: str) -> None:
            self.firstName = firstName
            self.secondName = secondName

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, Pythonista):
                return NotImplemented
            return ((self.firstName.lower() , self.secondName.lower() ) == (other.firstName.lower(), other.secondName.lower()))

        def __lt__(self, other: object) -> bool:
            if not isinstance(other, Pythonista):
                return NotImplemented
            return ((self.firstName.lower() , self.secondName.lower() ) < (other.firstName.lower(), other.secondName.lower()))


    guido = Pythonista("Guido", "van Rossum")
    brett = Pythonista("Brett", "Cannon")
    print(guido > brett)
            

    

    
    
    
                  
                  

    
