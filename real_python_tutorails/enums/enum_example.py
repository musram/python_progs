#https://florian-dahlitz.de/blog/why-you-should-use-more-enums-in-python


"""
enum stands for enumeration and refers to a set of symbolic names, which are called enumeration members. These enum members are bound to unique, constant values. You can iterate over an enumeration and compare its members by identity
"""

from enum import Enum

class Colour(Enum):
    RED=1
    GREEN=2
    BLUE=3



if __name__ == "__main__":
    c = Colour.RED

    print(c)
    print(c.name)
    print(c.value)
    print(c is Colour.RED)
    print(c is Colour.GREEN)


    """
    Enumerations have a special attribute called __members__, which is a read-only ordered mapping of names and members. Utilising __members__ allows you to iterate over an enum and print the members as well as their corresponding names.
    """

    for name, member in Colour.__members__.items():
        print(name, member)

    """
    Automatic values
In the previous example, we assigned integers to the symbolic names RED, GREEN, and BLUE. If the exact values are not important, you can use the enum.auto() function. The function calls _generate_next_value_() internally and generates the values for you.
    """

    from enum import auto

    class Colour(Enum):
        RED = auto()
        GREEN = auto()
        BLUE = auto()

    c = Colour.RED
    print(c.value)


    class AutoName(Enum):
        def _generate_next_value_(name, start, count, last_values):
            if len(last_values) > 0:
                return last_values[-1] * 2
            return 2


    class Colour(AutoName):
        RED = auto()
        GREEN = auto()
        BLUE = auto()

    c = Colour.RED
    g = Colour.GREEN
    b = Colour.BLUE

    print(c.value)
    print(g.value)
    print(b.value)

    """
    Being Python classes, enums can have any (special) methods just like all other classes. Consider the following example.

    """
    class Colour(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3

        def __str__(self):
            return self.name

        def colorize(self):
            return f"Let's paint everything in {self.name.lower()}"

    c = Colour.RED
    print(c)
    print(c.colorize())


    r = Colour.RED
    b = Colour.GREEN

    try:
        print(r < b)
    except TypeError as e:
        print(e)

    """
    The only thing you can do is making use of equality comparisons like == and !=. Additionally, comparing enum members with any non-enumeration value is not supported
    """
    from enum import IntEnum


    class Colour(IntEnum):
        RED = 1
        GREEN = 2
        BLUE = 3

    c = Colour.RED
    b = Colour.BLUE

    print( c< b)

    """
    The IntFlag class is pretty similar to the IntEnum class with the exception that is also supports bitwise operations. With supporting bitwise operations I mean that it is possible to combine two enum members resulting in an IntFlag member, too. All other operations on an IntFlag member will result in the loss of the IntFlag membership.

Let
s have a look at an example. Assume that we grant permissions to users so that they can read, write and/or execute a certain file. We create an enumeration Permission with the members R (read permission), W (write permission), and X (execute permission) respectively.

If we have a user, who should have read and write permissions for a certain file, we can combine both using the | operator.
    """
    from enum import IntFlag


    class Permission(IntFlag):
        R = 4
        W = 2
        X = 1


    RW = Permission.R | Permission.W
    print(RW)
    print(Permission.R + Permission.W)
    print(Permission.R in RW)


    """
    The Flag class does also provide support for bitwise operations but does not inherit from int. In fact, it is like Enum but with support for the bitwise operations.

If we take the Colour enum from the beginning, we could easily mix the colour white based on the other three colours.
    """

    from enum import auto
    from enum import Flag


    class Colour(Flag):
        RED = auto()
        GREEN = auto()
        BLUE = auto()
        WHITE = RED | GREEN | BLUE


    print(Colour.WHITE.name, Colour.WHITE.value)


    """
    Why we need it?
    """

    # response_code_magic_numbers.py

    from http.client import HTTPResponse


    def evaluate_response(response: HTTPResponse) -> str:
        if response.code() == 404:
            return "Not Found"
        elif response.code() == 502:
            return "???"
        elif response.code() == 400:
            return "???"
        else:
            return "Unknown Status Code"

    from enum import IntEnum
    class HTTPCode(IntEnum):
        BAD_REQUEST = 400
        NOT_FOUND = 404
        BAD_GATEWAY = 502


    def evaluate_response(response: HTTPResponse) -> str:
        if response.code() == HTTPCode.NOT_FOUND:
            return "Not Found"
        elif response.code() == HTTPCode.BAD_GATEWAY:
            return "???"
        elif response.code() == HTTPCode.BAD_REQUEST:
            return "???"
        else:
            return "Unknown Status Code"
