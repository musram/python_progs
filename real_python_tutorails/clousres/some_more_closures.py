



if __name__ == "__main__":

    #free variables

    def main_func():
        count = 0

        def inc():

            count += 1

            return count
        print(inc())
        print(inc())

    try:    
        main_func()
    except UnboundLocalError as e:
        print(e)


    def main_func():
        count = 10

        def inc():
            nonlocal count
            count += 1

            return count
        print(inc())
        print(inc())
        count = 20
        print(inc())
        print(inc.__code__.co_freevars)   # free variables. Mean count is declared somewhere and the accessed somewhere else.

        

    main_func()

    """
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    
    try:
        inc()
    except SyntaxError as e:
        print(e)


    """

    """
    In Python, a variable declared outside of the function or in global scope is known as a global variable. This means that a global variable can be accessed inside or outside of the function.
    """
    count = 0    #global variable
    def inc():
        global count    #it says that count refers to global count
        count += 1
        return count

    inc()
    print("count", count)

    print(inc.__code__.co_freevars)
    print(inc.__globals__)


    """
    The output shows an error because Python treats x as a local variable and x is also not defined inside foo().
    """
    
    x = "global"

    def foo():
        x = x * 2
        print(x)

    try:    
        foo()
    except UnboundLocalError as e:
        print(e)

    """
    A variable declared inside the function's body or in the local scope is known as local variable.
    """

    def foo():
        y = "local"

    foo()
    try:
        print(y)
    except NameError as e:
        print(e)

    """
    using local and global variables at same time
    """
    x = "global"

    def foo():
        global x
        y = "local"
        x = x * 2
        print(x)
        print(y)
 
    foo()


    """
    same name for gobal and local variable
    """

    x = 5

    def foo():
        x = 10
        print("local x:", x)

    foo()
    print("global x:", x)

    """
    create nonlocal varaible. Nonlocal variable are used in nested function whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.
    """
    def outer():
        x = "local"
 
        def inner():
            nonlocal x
            x = "nonlocal"
            print("inner:", x)
 
        inner()
        print("outer:", x)
    outer()

    x = 1
    def make_closures():
        x = 2
        def close():
            print(x)
        return close

    c  = make_closures()
    c()
    print(x)

    print(c.__code__.co_freevars)

    print(c.__code__.co_cellvars)

    print(make_closures.__code__.co_freevars)

    print(make_closures.__code__.co_cellvars)

    print(c.__closure__)



    def inc_generator(start=0):
        def inc(amnt=1):
            nonlocal start
            start +=  amnt
            return start
        return inc


    inc = inc_generator()

    print(inc())

    print(inc())

    #print(start)

    # same as above. So closures are objects
    class inc_class:
        def __init__(self,start=0):
            self.start = start

        def __call__(self,amnt=1):
            self.start += amnt
            return self.start

    inc = inc_class()

    print(inc())
    print(inc())
    

