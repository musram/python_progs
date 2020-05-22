#https://realpython.com/lessons/dynamic-vs-static/



if __name__ == "__main__":

    """
    Python is a dynamically typed language. This means that the Python interpreter does type checking only as code runs, and the type of a variable is allowed to change over its lifetime.
    """
    def check():
        if False:
            return 1 + 'two' # This line never runs, so no TypeError is raised
        else:
            return 1 + 2

    print(check())

    try:

        print( 1 + 'two')   # This is type checked

    except TypeError as e:
        print(e)


    thing = "hello"
    print(type(thing))

    thing = 28.1
    print(type(thing))

    """
    The opposite of dynamic typing is static typing. Static type checks are performed without running the program. In most statically typed languages, for instance C and Java, this is done as your program is compiled. The type of a variable is not allowed to change over its lifetime.
    """

    #Ducktyping

    """
    Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines. When you use duck typing, you do not check types at all. Instead, you check for the presence of a given method or attribute.
    """

    class TheHobbit:
        def __len__(self):
            return 9222

    the_hobbit = TheHobbit()

    print(the_hobbit)

    print(len(the_hobbit))

    my_str = "Hello World"
    my_list = [34, 54, 65, 78]
    my_dict = {"one": 123, "two": 456, "three": 789}
            
    print(len(my_str))
    print(my_str.__len__())

    print(len(my_list))

    print(len(my_dict))

    my_int = 7

    try:
        print(len(my_int))
    except TypeError as e:
        print(e)

    """
    In order for you to call len(obj), the only real constraint on obj is that it must define a .__len__() method. Otherwise, the object can be of types as different as str, list, dict, or TheHobbit
    """

    #type hinting

    def greet(name: str) -> str:
        return "hello, " + name

    print(greet("sai"))


    #Annotations

    #def func(arg: arg_type, optarg: arg_type = default) -> return_type:


    import math

    def circumference(radius: float) -> float:
        return 2 * math.pi * radius

    print(circumference.__annotations__)


    from typing import Dict, List, Tuple

    names: List[str] = ["Guido", "Thomas", "Bobby"]
    version: Tuple[int, int, int] = (3, 7, 1)
    options: Dict[str, bool] = {"centered": False, "capitalize": True}


    print(__annotations__)
