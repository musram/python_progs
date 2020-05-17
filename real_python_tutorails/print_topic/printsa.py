


if __name__ == "__main__":


    #Three ways to declare string

    var = 'I am god'
    var = "I am god"
    var = """ I am  god """

    # supporting two types of string allows to putting quote in a string easier
    var = ' hellow "sai" bye'

    print(var)

    print(70*'=')
    
    print( " my name \n is \n sai")



    print(" hi i am " + str(1))
    print('i', 6,  'memeners of')
    print('i', 6,  'memeners of', sep=' ')
    print('i', 6,  'memeners of', sep='\n')
    print('i', 6,  'memeners of', sep=None)


    # print() adds a \n at the end of what is being printed. This can be changed with the end parameter. Output from print() goes into a buffer. When you change the end parameter, the buffer no longer gets flushed. To ensure that you get output as soon as print() is called, you also need to use the flush=True parameter:


    import time

    def count_items(items):
        print('Counting ', end='', flush=True)
        num = 0
        for item in items:
            num += 1
            time.sleep(1)
            print('.', end='', flush=True)

        print('\nThere were {} items'.format(num))


    data = [ 
        ['year', 'last', 'first'], 
        [1943, 'Idle', 'Eric'], 
        [1939, 'Cleese', 'John'] 
        ]

    for row in data:
        print(*row, sep = ' ')


    #print() normally prints to the <stdout> file stream. You can change this behavior using the file parameter. You can access the <stdout> stream directly from the sys library:

    import sys

    result = sys.stdout.write('hello\n')

    print(result)

    #to write to file

    with open('file.txt', mode='w') as f:
        print('hello world', file=f)


    #When you pass an object to print(), it converts it to a string using the str() function. You can create a __str__() method on your custom objects to change what is output:

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return 'Person({})'.format(self.name)

        def __repr__(self):
            return 'Person(name={}, age={}'.format( self.name, self.age)
           

    john = Person('john Cllese', 80)
    print(john)

    #The __str__() method is meant to output a human-readable version of your object. There is also a __repr__() method, which is meant for a Python representation of the object. There is a repr() function that corresponds to the str() function. If you define your __repr__() properly, then eval() can be called on its result to create a new object.


    print(repr(john))

    #john2 = eval(repr(john))

    #print(type(john2))

    #print(id(john))

    #print(id(john2))


    #Some terminals support the ability to pass in special escape sequences to alter the color, weight, and appearance of the text being printed.

    #print('this is ', esc('31'), 'really', esc(0), ' important', sep='')

    #print('this is ', esc('31;1'), 'really', esc(0), ' important', sep='')

    #print('this is ', esc('31;1;4'), 'really', esc(0), ' important', sep='')



    #for real project print is not useful

    import logging, sys
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    def count_lower_case(item):
        logger.info('count_lower_case(%s)', item)
        num = 0
        for letter in item:
            if 97 <= ord(letter) <= 122:
                logger.debug('  letter *%s* is lowercase', letter)
                num += 1

        logger.info('  returning %s', num)
        return num

    count_lower_case('AbCdE')
