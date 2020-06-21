




if __name__ == "__main__":

    #closures tempalte
    def specialize(func, *outer_args, **outer_kwargs):
        def out(*args, **kwargs):
            return func(*(*args, *outer_args), **(**kwargs, **outer_kwargs))
        return out



    #closures are objects

    class Specialze1:
        def __init__(self, func, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.func = func

        def __call__(self, *args, **kwargs):
            return self.func(*(*args, *self.args), **(**kwargs, **self.kwargs))

    #The above definition of is same as partial function of functools

    #decorators are subset of closures

    
