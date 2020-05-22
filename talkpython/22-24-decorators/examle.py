from functools import wraps





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
