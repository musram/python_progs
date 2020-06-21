from urllib.request import urlopen
class UrlTemplate:
    def __init__(self, template):
        self.template = template
    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))

#class to function

def UrlTemplate(template):
    def opener(**kwargs):
        return urlopen(self.template.format_map(kwargs))
    return opener


if __name__ == "__main__":
    
    def apply_async(func, args, *, callback):
        # Compute the result
        result = func(*args)
        # Invoke the callback with the result
        callback(result)

    def print_result(result):
        print('Got:', result)

    def add(x, y):
        return x + y
    

    #storing states

    #in class

    class ResultHandler:
        def __init__(self):
            self.sequence = 0

        def handler(self, result):
            self.sequence += 1
            print(f"{self.sequence} Got {result}")

    

    #in function

    def ResultHandler():
        sequence = 0

        def handler(result):
            nonlocal sequence
            sequence += 1

            print(f"{self.sequence} Got {result}")

        return handler

    #using coroutines

    def ResultHandler():
        sequence = 0
        while True:
            result = yield

            sequence += 1
            print(f"{self.sequence} Got {result}")


        
    #h = ResultHandler()
    #apply_async(add, (2,3), callback=h.send)
    
    #using partials

    class SequenceNo:
        def __init__(self):
            self.sequence = 0

    def handler(result, seq):
        seq.sequence += 1
        print(f"{seq.sequence} Got {result}")

    seq = SequenceNo()
    from functools import partial
    apply_async(add, (2, 3), callback=partial(handler, seq=seq))





    #7.12


    def sample():

        n = 0

        def func():                         # closures
            print(f"n = {n}")

        def get_n():
            return n

        def set_n(value):
            nonlocal n             #First, nonlocal declarations make it possible to write functions that change inner variables
            n = value

        func.get_n = get_n         #Second, function attributes allow the accessor methods to be attached to the closure function in a straight forward manner where they work a lot like instance methods (even though no class is involved)
        func.set_n = set_n

        return func

    f = sample()
    f()

    print(f.get_n())

    f.set_n(3)

    f()

    print(f.get_n())
    
            
