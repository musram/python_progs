#https://realpython.com/python-modules-packages/

import mod
import sys



if __name__ == "__main__":
    print(mod.s)

    x = mod.Foo()
    print(x)

    print(sys.path)

    #to add to specific path
    #sys.path.append(r'/home/msr/books/python/')


    #Once a module has been imported, you can determine the location where it was found with the modules __file__ attribute

    print(mod.__file__)



    import re
    print(re.__file__)

    print(mod)


    #Each module has its own private symbol table, which serves as the global symbol table for all objects defined in the module. Thus, a module creates a separate namespace, as already noted.

    #Each module has its own private symbol table, which serves as the global symbol table for all objects defined in the module. Thus, a module creates a separate namespace, as already noted.

    try:
        print(s)
        print(a)
    except NameError as e:
        print(e)

    from mod import s,a

    #Because this form of import places the object names directly into the callers symbol table, any objects that already exist with the same name will be overwritten:

    print(s)
    print(a)

    from mod import *
    #This will place the names of all objects from <module_name> into the local symbol table, with the exception of any that begin with the underscore (_) character.This isnt necessarily recommended in large-scale production code. Its a bit dangerous because you are entering names into the local symbol table en masse. Unless you know them all well and can be confident there wont be a conflict, you have a decent chance of overwriting an existing name inadvertently.


    

    from mod import s as strings, a as alist

    s = 'foo'

    a = ['foo', 'bar']

    print(a)
    print(s)
    print(strings)
    print(alist)


    import mod as my_module
    print(my_module.a)

    #Lastly, a try statement with an except ImportError clause can be used to guard against unsuccessful import attempts

    try:

        import baz
    except ImportError as e:
        print(e)

    try:

        from mod import baz
    except ImportError as e:
        print(e)


    #dir() functions. Note how the first call to dir() above lists several names that are automatically defined and already in the namespace when the interpreter starts.

    print(dir())

    class Boo:
        pass

    x = Boo()

    print(dir())

    qux = [1, 2, 3, 4, 5]

    print(dir())


    print(dir(mod))


    #When a .py file is imported as a module, Python sets the special dunder variable __name__ to the name of the module. However, if a file is run as a standalone script, __name__ is (creatively) set to the string __main__. Using this fact, you can discern which is the case at run-time and alter behavior accordingly:


    from fact import fact

    print(fact(5))


    #reloading the module
    #For reasons of efficiency, a module is only loaded once per interpreter session. That is fine for function and class definitions, which typically make up the bulk of a modules contents. But a module can contain executable statements as well, usually for initialization. Be aware that these statements will only be executed the first time a module is imported.


    import importlib
    importlib.reload(mod)
    
    #packages


    from pkg import mod1
    print(mod1.foo())

    import pkg.mod1, pkg.mod2
    print(pkg.mod1.foo())

    from pkg.mod1 import foo
    print(foo())

    from pkg import mod2 as quux
    print(quux.bar())

    import pkg


    try:

        print(pkg.mod1)

    except AttributeError as e:
        print(e)
    

    
    #using __init__.py

    import pkg2

    print(pkg2.A)


    from pkg2 import mod1

    print(mod1.foo())


    #__init__.py can also be used to effect automatic importing of modules from a package. For example, earlier you saw that the statement import pkg only places the name pkg in the callers local symbol table and doesnt import any modules. But if __init__.py in the pkg directory contains the following:

    #import pkg2.mod1, pkg2.mod2  in  __init__.py
    #import pkg2
    print(pkg2.mod1.foo())




    from pkg3 import *

    print(dir())  # does not import pkg3

    #if the __init__.py file in the package directory contains a list named __all__, it is taken to be a list of modules that should be imported when the statement from <package_name> import * is encountered.

    
    #By the way, __all__ can be defined in a module as well and serves the same purpose: to control what is imported with import *.

    '''
    In mod1.py we can write __all__ = ['foo']

    def foo():
        print('[mod1] foo()')

    class Foo:
        pass
    '''


    '''
    In summary, __all__ is used by both packages and modules to control what is imported when import * is specified. But the default behavior differs:

For a package, when __all__ is not defined, import * does not import anything.
For a module, when __all__ is not defined, import * imports everything (except you guessed it names starting with an underscore).

    '''

    import pkg4.subpkg1.mod1

    print(pkg4.subpkg1.mod1.foo())


    from pkg4.subpkg1 import mod2
    print(mod2.bar())

    from pkg4.subpkg2.mod3 import baz
    print(baz())

    from pkg4.subpkg2.mod4 import qux as grault
    print(grault())



    '''
    Or you can use a relative import, where .. refers to the package one level up. From within mod3.py, which is in subpackage sub_pkg2,

.. evaluates to the parent package (pkg), and
..sub_pkg1 evaluates to subpackage sub_pkg1 of the parent package.

   '''

    

    
