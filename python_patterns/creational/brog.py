"""
*What is this pattern about?
The Borg pattern (also known as the Monostate pattern) is a way to
implement singleton behavior, but instead of having only one instance
of a class, there are multiple instances that share the same state. In
other words, the focus is on sharing state instead of sharing instance
identity.
*What does this example do?
To understand the implementation of this pattern in Python, it is
important to know that, in Python, instance attributes are stored in a
attribute dictionary called __dict__. Usually, each instance will have
its own dictionary, but the Borg pattern modifies this so that all
instances have the same dictionary.
In this example, the __shared_state attribute will be the dictionary
shared between all instances, and this is ensured by assigining
__shared_state to the __dict__ variable when initializing a new
instance (i.e., in the __init__ method). Other attributes are usually
added to the instance's attribute dictionary, but, since the attribute
dictionary itself is shared (which is __shared_state), all other
attributes will also be shared.
*Where is the pattern used practically?
Sharing state is useful in applications like managing database connections:
https://github.com/onetwopunch/pythonDbTemplate/blob/master/database.py
*References:
https://fkromer.github.io/python-pattern-references/design/#singleton
*TL;DR
Provides singleton-like behavior sharing state between instances.
"""




class Brog:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state

class YourBorg(Brog):
    pass


if __name__ == "__main__":
    rm1 = Brog()
    rm2 = Brog()
    print(rm1.__dict__)
    print(rm2.__dict__)
    #print(Brog.__shared_state)

    print(id(rm1))
    print(id(rm2))

    rm2.state = 'Running'
    print(rm1.__dict__)
    print(rm2.__dict__)

    print( rm1 == rm2)

    rm3 = Brog()
    print(rm1.__dict__)
    print(rm2.__dict__)
    print(rm3.__dict__)

    
