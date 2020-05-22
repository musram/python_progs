from functools import wraps
import time





if __name__ == "__main__":

    #template
    def mydecorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
                # do something before the original function is called
                # call the passed in function
                result = function(*args, **kwargs)
                # do something after the original function call
                return result
        # return wrapper = decorated function
        return wrapper

    @mydecorator
    def my_function(args):
        pass

    #This is just syntactic sugar for:

    def my_function(args):
        pass

    my_function = mydecorator(my_function)



    def get_profile(name, active=True, *sports, **awards):
        print('Positional arguments (required): ', name)
        print('Keyword arguments (not required, default values): ', active)
        print('Arbitrary argument list (sports): ', sports)
        print('Arbitrary keyword argument dictionary (awards): ', awards)


    get_profile('julian')

    get_profile('julian', active=False)

    get_profile('julian', False, 'basketball', 'soccer')

    get_profile('julian', False, 'basketball', 'soccer',
            pythonista='special honor of the community', topcoder='2017 code camp')

    def show_args(function):
        @wraps(function)
        def wrapper(*args, **kwargs):     
            print('hi from decorator - args:')
            print(args)
            result = function(*args, **kwargs)
            print('hi again from decorator - kwargs:')
            print(kwargs)
            return result
        # return wrapper as a decorated function
        return wrapper


    @show_args
    def get_profile(name, active=True, *sports, **awards):
        print('\n\thi from the get_profile function\n')


    get_profile('bob', True, 'basketball', 'soccer', 
            pythonista='special honor of the community', topcoder='2017 code camp')



    def timeit(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('== starting timer')
            start = time.time()

            func(*args, **kwargs)

            end = time.time()

            print(f'== {func.__name__} took {int(end-start)} seconds to complete')

        return wrapper


    @timeit
    def generate_report():
        '''Function to generate revenue report'''
        time.sleep(2)
        print('(actual function) Done, report links ...')

    generate_report()


    print(generate_report.__doc__)


    #stacked

    def print_args(func):
        '''Decorator to print function arguments'''
        @wraps(func)
        def wrapper(*args, **kwargs):
        
            # before
            print()
            print('*** args:')
            for arg in args:
                print(f'- {arg}')
        
            print('**** kwargs:')
            for k, v in kwargs.items():
                print(f'- {k}: {v}')
            print()
        
            # call func
            func(*args, **kwargs)
        return wrapper


    @timeit
    @print_args
    def generate_report(*months, **parameters):
        time.sleep(2)
        print('(actual function) Done, report links ...')

    generate_report()

    parameters = dict(split_geos=True, include_suborgs=False, tax_rate=33)

    generate_report('October', 'November', 'December', **parameters)


    def make_html(tag_name):
        def tag_decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                return "<{}>  {} </{}>".format(tag_name, func(*args, **kwargs), tag_name)
            return wrapper
        return tag_decorator

    
    def tags(tag_name):
        def tags_decorator(func):
            @wraps(func)
            def func_wrapper(name):
                return "<{0}>{1}</{0}>".format(tag_name, func(name))
            return func_wrapper
        return tags_decorator



    @make_html('p')
    @make_html('strong')
    #@tags('p')
    def get_text(text):
      return text

    print(get_text('I code with PyBites'))

