def baz():
    print('[mod3] baz()')

class Baz:
    pass


#from pkg4.subpkg1.mod1 import foo
#foo()

#or

from .. import subpkg1
print(subpkg1)

from ..subpkg1.mod1 import foo
foo()
