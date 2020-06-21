if __name__ == "__main__":

    from functools import wraps


    class A:
        def decorator1(self, func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                print(f"Decorator 1")
                return func(*args, **kwargs)
            return wrapper

        @classmethod
        def decorator2(cls, func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                print(f"Decorator 2")
                return func(*args, **kwargs)
            return wrapper


    a  = A()

    @a.decorator1
    def spam():
        pass

    spam()
    
    @A.decorator2
    def grok():
        pass

    grok()


    class B(A):

        @A.decorator2
        def bar(self):
            pass

    b = B()
    b.bar()
