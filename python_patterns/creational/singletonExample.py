#from __future__ import annotations
from typing import Optional



'''
class Tigger:

    def __str__(self):
        return "I'm the only one!"

    def roar(self):
        return 'Grrr!'
'''

#singleton methods
class _Tigger:
    def __str__(self):
        return "I'm the only one!"

    def roar(self):
        return 'Grrr!'

_instance = None

def Tigger():
    global _instance
    if _instance is None:
        _instance = _Tigger()
    return _instance    

# alternative singleton
class Singleton:
   __instance = None
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self




#alternative
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """
    def __init__(self, *args, **kwargs):
        self._instance = None
        super().__init__(*args, **kwargs)
        

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
            return self._instance
        else:
            return self._instance


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...    


if __name__ == "__main__":
    a = Tigger()
    b = Tigger()

    print(id(a))
    print(id(b))

    print(a == b)

    print(a)

    print(b)

    print(b.roar())
