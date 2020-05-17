from functools import wraps


#decorator
def logged(func):
    @wraps(func)
    def wrapper(*args ,  **kwargs):
        print('you called function {} with {} and {}'.format(func.__name__, args, kwargs))
        print('it returned {}'.format(func(*args, **kwargs)))
        return func(*args, **kwargs)
    return wrapper





if __name__ == "__main__":
    @logged
    def func2(a=None, b= None):
        return None

    func2()
    func2(3, b=2)



    f = lambda: map((yield), range(10))
    for x in f():
        print(x)

    def f1():
        yield

    for x in f1():
        print(x)


        
        






    #generator

    def gen():
        for i in range(10):
            yield i;


    g = gen()
    print(next(g))
    print(next(g))


    g_alternate = ( i for i in range(10))

    print(next(g_alternate))
    print(next(g_alternate))

    import random

    def randomized(seq):
        random.shuffle(seq)
        for i in seq:
            yield i


    def counter(n):
    i = 1
    while i <= n:
        yield i
        i += 1

    def print_table():
        outer = counter(10)
        finished = False               # <---- get rid of this
        total, limit = 0, 100
        for i in outer:
            inner = counter(i)
            print(i, end=': ')
            for j in inner:
                print(i * j, end=' ')
                total += i * j
                if total >= limit:
                    finished = True    # <----- and this
                    break
        print()
        if finished:               # <----- and also this
            break                  #
        print('total:', total)
    
    def print_table():
        outer = counter(10)
        # <---- get rid of this
        total, limit = 0, 100
        for i in outer:
            inner = counter(i)
            print(i, end=': ')
            for j in inner:
                print(i * j, end=' ')
                total += i * j
                if total >= limit:
                    outer.close()    # <----- and this
                    break
        print()
        # <----- and also this
        print('total:', total)
    
