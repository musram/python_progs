



if __name__ == "__main__":
    class Foo:
        foobar = 2

    f = Foo()

    print(dir(f))
    print(dir(Foo))

    print(f.__dict__)
    print(Foo.__dict__)

        
    print(Foo.__dict__['foobar'])

    f.__setattr__('name', 'sai')
    print(f.__dict__)

    print(f.__getattribute__('name'))


    