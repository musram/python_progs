




if __name__ == "__main__":

    """
    A bytes literal is defined in the same way as a string literal with the addition of a 'b' prefix. Single, double, or triple quoting mechanisms can be used. Only ASCII characters are allowed, and any character value greater than 127 must be specified using an appropriate escape sequence. The 'r' prefix can be used to disable processing of escape sequences

    """
    a = b'spam egg bacon'
    print(a)
    print(type(a))

    c = b"Contain embedded 'single' quotes"
    print(c)
    print(type(c))


    t = b'''This bytes object contains "double" and 'single' quotes!'''
    print(t)
    print(type(t))


    a = b'spam\xddegg'
    print(list(a))

    print(a[0])

    a = rb'spam\xddegg'
    print(a)
    print(len(a))

    b = b'spam\xddegg'
    print(len(b))


    """
    Youll explore three different forms of using bytes():

    bytes(<s>, <encoding>) creates a bytes object from a string.
    bytes(<size>) creates a bytes object consisting of null (0x00) bytes.
    bytes(<iterable>) creates a bytes object from an iterable.
    """

    a = bytes('bacon and egg', 'utf8')
    print(a)
    print(type(a))
    print(len(b))
    print(a[0])

    a = bytes(8)
    print(a)
    print(type(a))

    d = bytes([115, 112, 97, 109, 33])
    print(d)
    print(type(d))


    #common sequence operations that bytes objects support

    #how to use the in and not in operators:

    a = b'abcde'

    print(b'ab' in a)
    print(b'spam' in a)
    print(b'spam' not in a)


    #use the concatenation (+) and replication (*) operators:
    a = b'abcde'
    b = b'fghij'

    print(a+b)

    print(a*3)

    #how to do indexing and slicing

    print(a[1])

    print(a[2:-1])

    #built-in functions

    print(min(a))
    print(max(a))
    print(len(a))
    print(chr(101))

    a = b'spam,egg,spam,bacon,spam,lobster'

    print(a.count(b'spam'))

    try:
        print(a.count('spam'))
    except TypeError as e:
        print(e)

    print(a.endswith(b'ster'), a.find(b'bacon'), sep = " ")

    print(a.split(sep=b','))

    print(a.center(40, b'-'))


    #use bytes.fromhex(<s>) and b.hex()

    print(list(a))

    print(hex(a[0]))

    b = bytes.fromhex(' aa 68 32 af ')

    print(list(b))

    print(b)

    print(b.hex())

    print(type(b.hex()))

    """
    bytearray objects are very similar to bytes objects, despite these differences:

    There is no dedicated syntax for defining a bytearray literal.
    A bytearray is always created using the bytearray() built-in function.
    bytearray objects are mutable.
    """

    ba = bytearray('spam.egg.bacon', 'utf8')
    print(ba)

    print(type(ba))

    ba2 = bytearray(6)
    print(ba2)

    ba3 = bytearray([97, 98, 99, 100, 101])
    print(ba3)

    ba3[4] = 0xee
    print(ba3)

    ba3[:3] = b'egg'
    print(ba3)

    ba4 = bytearray(b'spam')
    print(ba4)



    #convert bytesarray to bytes
    print(bytes(ba4))
    

