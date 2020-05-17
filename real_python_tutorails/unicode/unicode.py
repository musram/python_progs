#https://realpython.com/python-encodings-guide/





if __name__ == "__main__":

    #ASCII contains 128 characters.

    #From lib/python3.7/string.pyx
    
    #whitespace = ' \t\n\r\v\f'
    #ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    #ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #ascii_letters = ascii_lowercase + ascii_uppercase
    #digits = '0123456789'
    #hexdigits = digits + 'abcdef' + 'ABCDEF'
    #octdigits = '01234567'
    #punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    #printable = digits + ascii_letters + punctuation + whitespace


    def make_bitseq(str):
        if not str.isascii():
            raise ValueError("ASCII only allowed")
        return " ".join('{:08b}'.format(ord(i)) for i in str)

    print(make_bitseq("bits"))

    def make_octseq(str):
        if not str.isascii():
            raise ValueError("ASCII only allowed")
        return " ".join('{:08b}'.format(ord(i)) for i in str)

    print(make_bitseq("bits"))

    def make_bitseq(str):
        if not str.isascii():
            raise ValueError("ASCII only allowed")
        return " ".join('{:08b}'.format(ord(i)) for i in str)

    print(make_bitseq("bits"))
    

    #number systems

    print(int('11'))

    print(int('11', base = 10))
    print(int('11', base = 2))
    print(int('11', base = 8))
    print(int('11', base = 16))


     #bytes or str to str

    def to_str(bytes_or_str):
        if isinstance(bytes_or_str , bytes):
            value = bytes_or_str.decode('utf-8')
        else:
            value = bytes_or_str
        return value

    print(repr(to_str(b'foo')))
    print(repr(to_str('bar')))


    #bytes or str to bytes

    def to_bytes(bytes_or_str):
        if isinstance(bytes_or_str , str):
            value = bytes_or_str.encode('utf-8')
        else:
            value = bytes_or_str
        return value

    print(repr(to_bytes(b'foo')))
    print(repr(to_bytes('bar')))


    #By using the + operator, you can add bytes to bytes and str to str, respectively:

    print(b'one' + b'two')
    print('one' + 'two')

    try:
        print('one' + b'two')

    except TypeError as e:
        print(e)


    #By using binary operators, you can compare bytes to bytes and str to str, respectively:


    assert b'red' > b'blue'
    assert 'red' > 'blue'

    try:
        assert b'red' > 'red'
    except AssertionError as e:
        print(e)
    except TypeError as e:
        print(e)

    try:
        assert b'red' == 'red'
    except AssertionError as e:
        print(e)
    except TypeError as e:
        print(e)

    #When a file is in text mode, write operations expect str instances containing Unicode data instead of bytes instances containing binary data. Here, I fix this by changing the open mode to 'wb'

    with open('data.bin' , 'wb') as f:
        f.write(b'\xf1\xf2\xf3\xf4\xf5')


    
    with open('data.bin', 'rb') as f:
        data = f.read()
        assert data == b'\xf1\xf2\xf3\xf4\xf5'
        
    
