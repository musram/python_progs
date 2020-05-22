#https://rednafi.github.io/digressions/python/2020/05/13/python-decorators.html#first-class-objects




if __name__ == "__main__":

    # Function as first class object
    """
    basically everything is an object and functions are regarded as first-class objects. It means that functions can be passed around and used as arguments, just like any other object (string, int, float, list, and so on). You can assign functions to variables and treat them like any other objects.
    """
    
    def func_a():
        return "I was angry with my friend"

    def func_b():
        return "I told my wrath, my wrath did end"


    def func_c(*funcs):
        for func in funcs:
            print(func())


    func_c(func_a, func_b)        

    #function as higher order function
    """
    Python also allows you to use functions as return values. You can take in another function and return that function or you can define a function within another function and return the inner function
    """

    def higher(func):
        """This is a higher order function.
        It returns another function.
        """

        return func


    def lower():
        return "I'm hunting high and low"

    print(higher(lower))

    h = higher(lower)
    print(h())

    def outer():
        """Define and return a nested function from another function."""

        def inner():
            return "Hello from the inner func"

        return inner


    inn = outer()
    print(inn())

    #closures
    """
    we saw examples of inner functions at work in the previous section. Nested functions can access variables of the enclosing scope. In Python, these non-local variables are read only by default and we must declare them explicitly as non-local (using nonlocal keyword) in order to modify them
    """

    def burger(name):
        def ingredients():
            if name == "deli":
                return ("steak", "pastrami", "emmental")
            elif name == "smashed":
                return ("chicken", "nacho cheese", "jalapeno")
            else:
                return None

        return ingredients


    ingr = burger("deli")
    print(ingr())

    """
    The burger function was called with the string deli and the returned function was bound to the name ingr. On calling ingr(), the message was still remembered and used to derive the outcome although the outer function burger had already finished its execution.This technique by which some data (deli) gets attached to the code is called closure in Python. The value in the enclosing scope is remembered even when the variable goes out of scope or the function itself is removed from the current namespace. Decorators uses the idea of non-local variables multiple times.
    """


    #basic decorators

    def deco(func):
        def wrapper():
            print("This will get printed before the function is called.")
            func()
            print("This will get printed after the function is called.")

        return wrapper


    def ans():
        print(42)


    ans = deco(ans)

    ans()

    """
    To put it simply, decorators wraps a function and modifies its behavior.

The decorator function runs at the time the decorated function is imported/defined, not when it is called.
    """

    def deco(func):
        """This modified decorator also returns the result of func."""

        def wrapper():
            print("This will get printed before the function is called.")
            val = func()
            print("This will get printed after the function is called.")
            return val

        return wrapper

    def ans():
        return 42

    ans = deco(ans)
    print(ans())


    #@ syntatics sugar

    #@deco
    #def func():
    #   pass

    #func() is same as func = deco(func)


    #decorating functions with arguments

    def yell(func):
        def wrapper(*args, **kwargs):
            val = func(*args, **kwargs)
            val = val.upper() + "!"
            return val

        return wrapper


    @yell
    def hello(name):
        return f'hello {name}'

    print(hello("redowna"))


    """
    The decorator yell has made the function hello confused about its own identity. Instead of reporting its own name, it takes the identity of the inner function wrapper. This can be confusing while doing debugging. You can fix this using builtin functools.wraps decorator. This will make sure that the original identity of the decorated function stays preserved.
    """

    print(hello.__name__)

    print(help(hello))



    import functools

    def yell(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            val = func(*args, **kwargs)
            val = val.upper() + "!"
            return val

        return wrapper


    @yell
    def hello(name):
        "Hello from the other side."
        return f'hello {name}'


    print(hello("Galaxy"))


    print(hello.__name__)

    print(help(hello))


    #template

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Do something before
            val = func(*args, **kwargs)
            # Do something after
            return val

        return wrapper



    #examples

    from datetime import datetime


    def logexc(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            # Stringify the arguments
            args_rep = [repr(arg) for arg in args]
            kwargs_rep = [f"{k}={v!r}" for k, v in kwargs.items()]
            sig = ", ".join(args_rep + kwargs_rep)

            # Try running the function
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print("Time: ", datetime.now().strftime("%Y-%m-%d [%H:%M:%S]"))
                print("Arguments: ", sig)
                print("Error:\n")
                #raise

        return wrapper
    
    @logexc
    def divint(a, b):
        return a / b

    divint(1,0)


    #validation and runtime check
    """
    Pythons type system is strongly typed, but very dynamic. For all its benefits, this means some bugs can try to creep in, which more statically typed languages (like Java) would catch at compile time. Looking beyond even that, you may want to enforce more sophisticated, custom checks on data going in or out. Decorators can let you easily handle all of this, and apply it to many functions at once.

Imagine this: you have a set of functions, each returning a dictionary, which (among other fields) includes a field called summary. The value of this summary must not be more than 30 characters long; if violated, thats an error.
    """

    def validate_summary(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            if len(data["summary"]) >30:
                raise ValueError("Summary exceeds 30")
            return data
        return wrapper


    @validate_summary
    def short_summary():
        return {"summary": "This is a short summary"}


    @validate_summary
    def long_summary():
        return {"summary": "This is a long summary that exceeds character limit."}

    print(short_summary())

    try:
        print(long_summary())
    except  ValueError as e:
        print(e)




    #one more application

    import requests


    def retry(func):
        """This will rerun the decorated callable 3 times if
        the callable encounters http 500/404 error."""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            n_tries = 3
            tries = 0
            while True:
                resp = func(*args, **kwargs)
                if resp.status_code == 500 or resp.status_code == 404 and tries < n_tries:
                    print(f"retrying... ({tries})")
                    tries += 1
                    continue
                break
            return resp

        return wrapper


    @retry
    def getdata(url):
        resp = requests.get(url)
        return resp


    resp = getdata("https://httpbin.org/get/1")
    print(resp.text)


    #multiple decorators

    def greet(func):
        """Greet in English."""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            val = func(*args, **kwargs)
            return "Hello " + val + "!"

        return wrapper


    def flare(func):
        """Add flares to the string."""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            val = func(*args, **kwargs)
            return "Hi" + val + "Iam finex"

        return wrapper


    @flare
    @greet
    def getname(name):
        return name


    #decorator with arguments

    def joinby(delimiter=" "):
        """This decorator splits the string output of the
        decorated function by a single space and then joins
        them using a user specified delimiter."""

        def outer_wrapper(func):
            @functools.wraps(func)
            def inner_wrapper(*args, **kwargs):
                val = func(*args, **kwargs)
                val = val.split(" ")
                val = delimiter.join(val)
                return val

            return inner_wrapper

        return outer_wrapper

    @joinby(delimiter=",")
    def hello(name):
        return f"Hello {name}!"

    @joinby(delimiter=">")
    def greet(name):
        return f"Greetings {name}!"

    @joinby()
    def goodbye(name):
        return f"Goodbye {name}!"

    print(hello("Nafi"))
    print(greet("Redowan"))
    print(goodbye("Delowar"))




    #decorators with or without arguments


    """
    Here, the _func argument acts as a marker, noting whether the decorator has been called with arguments or not:

If joinby has been called without arguments, the decorated function will be passed in as _func. If it has been called with arguments, then _func will be None. The * in the argument list means that the remaining arguments cant be called as positional arguments. This time you can use joinby with or without arguments and function hello and greet above demonstrate that.
    """

    def joinby(_func=None, *, delimiter=" "):
        """This decorator splits the string output
        of a function by a single space and then joins that
        using a user specified delimiter."""

        def outer_wrapper(func):
            @functools.wraps(func)
            def inner_wrapper(*args, **kwargs):
                val = func(*args, **kwargs)
                val = val.split(" ")
                val = delimiter.join(val)
                return val

            return inner_wrapper

        # This part enables you to use the decorator with/without arguments
        if _func is None:
            return outer_wrapper
        else:
            return outer_wrapper(_func)


    @joinby(delimiter=",")
    def hello(name):
        return f"Hello {name}!"


    @joinby
    def greet(name):
        return f"Greetings {name}!"


    print(hello("Nafi"))
    print(greet("Redowan"))


    #code made simple by partial

    def decorator(func=None, foo="spam"):
        if func is None:
            return functools.partial(decorator, foo=foo)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Do something with `func` and `foo`, if you're so inclined
            pass

        return wrapper


    # Applying decorator without any parameter
    @decorator
    def f(*args, **kwargs):
        pass


    # Applying decorator with extra parameter
    @decorator(foo="buzz")
    def f(*args, **kwargs):
        pass


    #retry examples

    def retry(func=None, n_tries=4):
        """This will rerun the decorated callable 3 times if
        the callable encounters http 500/404 error."""

        if func is None:
            return functools.partial(retry, n_tries=n_tries)
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            tries = 0
            while True:
                resp = func(*args, **kwargs)
                if resp.status_code == 500 or resp.status_code == 404 and tries < n_tries:
                    print(f"retrying... ({tries})")
                    tries += 1
                    continue
                break
            return resp

        return wrapper

    






    @retry
    def getdata(url):
        resp = requests.get(url)
        return resp


    @retry(n_tries=2)
    def getdata_(url):
        resp = requests.get(url)
        return resp

    resp1 = getdata("https://httpbin.org/get/1")

    print("-----------------------")
    resp2 = getdata_("https://httpbin.org/get/1")


    """
    In this case, you do not have to write three level nested functions and the functools.partial takes care of that. Partials can be used to make new derived functions that have some input parameters pre-assigned.Roughly partial does the following:
    """

    def partial(func, *part_args):
        def wrapper(*extra_args):
            args = list(part_args)
            args.extend(extra_args)
            return func(*args)

        return wrapper











    #defining decorators with class

    """
    Classes can be handy to avoid nested architecture while writing decorators. Also, it can be helpful to use a class while writing stateful decorators. You can follow the pattern below to compose decorators with classes.
    """
    #template
    class ClassDeco:
        def __init__(self, function):
            functools.update_wrapper(self, func)
            self.func = func

        def __call__(self, *args, **kwargs):

            # You can add some code before the function call
            val = self.func(*args, **kwargs)
            # You can also add some code after the function call

            return val


    """
    The init() method stores a reference to the function num_calls and can do other necessary initialization. The call() method will be called instead of the decorated function. It does essentially the same thing as the wrapper() function in our earlier examples. Note that you need to use the functools.update_wrapper() function instead of @functools.wraps
    """

    class Emphasis:
        def __init__(self, func):
            functools.update_wrapper(self, func)
            self.func = func

        def __call__(self, *args, **kwargs):
            val = self.func(*args, **kwargs)
            return "<b>" + val + "</b>"


    @Emphasis
    def hello(name):
        return f"Hello {name}"


    print(hello("Nafi"))
    print(hello("Redowan"))

    """
    Stateful decorators can remember the state of their previous run. Heres a stateful decorator called Tally that will keep track of the number of times decorated functions are called in a dictionary. The keys of the dictionary will hold the names of the functions and the corresponding values will hold the call count.
    """


    class Tally:
        def __init__(self, func):
            functools.update_wrapper(self, func)
            self.func = func
            self.tally = {}
            self.n_calls = 0

        def __call__(self, *args, **kwargs):
            self.n_calls += 1;
            self.tally[self.func.__name__] = self.n_calls

            print(f'callable tally {self.tally}')
            return self.func(*args, **kwargs)

    @Tally
    def hello(name):
        return f"Hello {name}!"


    print(hello("Redowan"))
    print(hello("Nafi"))



    #Caching Return Values
    """
    Decorators can provide an elegant way of memoizing function return values. Imagine you have an expensive API and youd like call that as few times as possible. The idea is to save and cache values returned by the API for particular arguments, so that if those arguments appear again, you can serve the results from the cache instead of calling the API again. This can dramatically improve your applications performance. Here Ive simulated an expensive API call and provided caching with a decorator.
    """

    import time
    
    def api(a):
        """API takes an integer and returns the square value of it.
        To simulate a time consuming process, I've added some time delay to it."""

        print("The API has been called...")

        # This will delay 3 seconds
        time.sleep(3)

        return a * a


    api(3)


    """
    To cache the result , we can use Pythons built in functools.lru_cache to save the result against an argument in a dictionary and serve that when it encounters the same argument again. The only drawback here is, all the arguments need to be hashable
    """



    """
    Least Recently Used (LRU) Cache organizes items in order of use, allowing you to quickly identify which item hasnt been used for the longest amount of time. In the above case, the parameter max_size refers to the maximum numbers of responses to be saved up before it starts deleting the earliest ones. While you run the decorated function, youll see first time itll take roughly 3 seconds to return the result. But if you rerun the function again with the same parameter itll spit the result from the cache almost instantly.
    """
   


    @functools.lru_cache(maxsize=32)
    def api(a):
        """API takes an integer and returns the square value of it.
        To simulate a time consuming process, I've added some time delay to it."""

        print("The API has been called...")

        # Thais will delay 3 seconds
        time.sleep(3)

        return a * a


    api(3)




    #application

    def convert(func=None, convert_to=None):
        if func is None:
            return functools.partial(convert, convert_to = convert_to)



        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Conversion unit: {convert_to}")

            val = func(*args,  **kwargs)

            if convert_to is None:
                return val

            elif convert_to == "Km":
                return val /1000
            
            elif convert_to == "mile":
                return val * 0.000621371

            elif convert_to == "cm":
                return val * 100

            elif convert_to == "mm":
                return val * 1000

            else:
                raise ValueError("Conversion unit is not supported.")

        return wrapper


    @convert(convert_to="mile")
    def area(a, b):
        return a * b


    print(area(1, 2))    