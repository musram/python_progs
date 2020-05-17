#https://realpython.com/lessons/case-conversion/




if __name__ == "__main__":
    s = 'egG BacOn SauSAGE loBSter'
    print(s.capitalize())

    print(s.lower())

    print(s.upper())

    print(s.swapcase())

    print(s.title())


    """
    In this lesson, youll explore string methods that provide various means of searching the target string for a specified substring.

Each method in this group supports optional <start> and <end> arguments. These are interpreted as for string slicing: the action of the method is restricted to the portion of the target string starting at character position <start> and proceeding up to but not including character position <end>. If <start> is specified but <end> is not, then the method applies to the portion of the target string from <start> through the end of the string.

    """

    s = 'spam ham clam jam'

    print(s.count('am'))
    print(s.count('am',0,9))

    print(s.endswith('jam'))

    print(s.endswith('ham', 0,8))

    print(s.startswith('spam'))

    print(s.startswith('ham', 5, 15))


    print(s.find('spam'))

    print(s.find('ham'))

    print(s.find('ham',  5, 15))

    s = 'spam bacon spam spam egg spam'

    print(s.find('spam'))

    print(s.rfind('spam'))

    print(s.rfind('spam', 8, 15))

    print(s.rfind('spam', 8, 10))

    print(s.index('spam'))

    print(s.rindex('spam'))

    print(s.index('egg'))



    #character classifcations

    s = 'abc123'
    print(s.isalnum())

    s = 'abc$123'
    print(s.isalnum())


    s = 'ABCabc'
    print(s.isalnum())

    s = 'ABC123'
    print(s.isalnum())

    s = '123456'
    print(s.isdigit())    

    s = '123abc'
    print(s.isdigit())

    #print('def'.identifier())

    from keyword import iskeyword

    print(iskeyword('def'))
    print(iskeyword('spam32'))


    s = 'a \n b'
    print(s.isspace())

    s = '\t\n '
    print(s.isspace())

    s = 'The Sun Also Rises'
    print(s.istitle())

    s = 'asdlkjgadb'
    print(s.islower())

    s = 'SPAMBACON'
    print(s.isupper())

    s = 'ABCabc#$%'
    #print(s.isascii())
    #print(''.isascii())
    #print(' '.isascii())


    #String Formatting

    s = 'spam'

    print(s.center(10))

    print(s.center(10, '-'))

    print(3, '-')

    s = 'a\tb\tc'

    print(s.expandtabs())

    print(s.expandtabs(4))

    print(s.ljust(10))

    print(s.ljust(10, '-'))

    print(s.ljust(3, '-'))

    print(s.rjust(10))

    print(s.rjust(10, '-'))

    print(s.rjust(3, '-'))


    s = '     spam bacon egg     '
    print(s.lstrip())

    t = '  \t  \n spam \t \n egg \t \n  '
    print(t.lstrip())

    link = 'http://www.realpython.com'
    print(link.lstrip('/:pth'))

    print(s.rstrip())

    print(t.rstrip())

    x = 'spam.$$$;'
    print(x.rstrip(';$.'))

    print(s.strip())

    print(t.strip())

    print(link.strip('w.moc'))

    print(link.strip(':/pth w.moc'))



    

    s = 'spam spam spam egg bacon spam spam lobster'
    print(s.replace('spam', 'tomato'))

    print(s.replace('spam', 'tomato', 3))


    s = '42'
    print(s.zfill(5))
    print(s.zfill(10))
    s = '+42'
    print(s.zfill(5))
    s = '-51'
    print(s.zfill(3))



    #converting between list and strings

    mylist = ['spam', 'egg', 'sausage', 'bacon', 'lobster']

    print(';'.join(mylist))

    print(','.join(mylist))

    word = 'lobster'

    print(type(word))

    print(','.join(word))

    mylist2 = ['spam', 23, 'egg']

    try:
        print(','.join(mylist2))
    except TypeError as e:
        print(e)
    
    mylist2 = ['spam', str(23), 'egg']

    try:
        print(','.join(mylist2))
    except TypeError as e:
        print(e)

    s = 'egg.spam'
    print(s.partition('.'))

    t = 'egg$$spam$$bacon'
    print(t.partition('$$'))

    print(t.rpartition('$$'))

    s = 'spam bacon sausage egg'

    print(s.split())

    s = 'spam\tbacon\nsausage egg'

    print(s.split())

    t = 'spam.bacon.sausage.egg'

    print(s.split('.'))

    t = 'bacon...lobster...bacon'
    print(t.split('.'))

    link = 'www.realpython.com'
    print(link.split('.'))

    print(link.split('.', maxsplit=1))

    print(link.rsplit('.', maxsplit=1))

    moby = 'Call me Ishmael.\nSome years ago- never mind how long precisely-\nhaving little or no money in my purse,\nand nothing particular to interest me on shore,\nI thought I would sail about a little and see the watery part of the world.\n'

    mobysplit = moby.splitlines()
    print(mobysplit[0])
    print(mobysplit[1])

    
    

    
