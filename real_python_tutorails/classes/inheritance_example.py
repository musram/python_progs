class Parent:
    def __init__(self, value):
        self.value = value

    def spam(self):
        print('parent.spam', self.value)
        self.spam()



#inheritance 1

class Child1(Parent):
    def yow(self):
        print('child.yow')

#inheritace 2
class Child2(Parent):
    def spam(self):
        print('child2.spam', self.value)

#inheritace 3

class child3(Parent):
    def spam(self):
        print('child3.spam')
        super().spam()

#inheritace 4
class child4(Parent):
    def __init__(self, value, extra):
        self.extra = extra
        super().__init__(value)

#inheritace 5

class Parent2:
    def yow(self):
        print('Parent2.yow')

class Child5(Parent, Parent2):
    pass


#How inheritance works


class Parent:
    def spam(self):
        print('Parent.spam')

class A(Parent):
    def spam(self):
        print('A.spam')
        super().spam()

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()

class C(Parent):
    def spam(self):
        print('C.spam')
        super().spam()
    
class D(Parent):
    def spam(self):
        print('D.spam')
        super().spam()

class F(A,C,D):
    pass

class E(D,C,A):
    pass



#abstract class

from abc import ABC, abstractmethod


class Point(ABC):
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    @abstractmethod
    def distance(self, destination_point):
        pass

    




if __name__ == "__main__":

    a = A()
    print(A.__mro__)   #prints hierarchy of inhertince


    #When inheritace there are two  rules
    #(1) for single inheritance the parent class has to be checked before the child. SO thats happend in B.__mro__


    print(B.__mro__)

    #(2) for multiple inheritace, the order of inheritance is the order in which multiple class is defined.

    f = F()
    f.spam()

    print(F.__mro__)

    e = E()
    e.spam()
    print(E.__mro__)

    try:
        p = Point(2,3)
    except TypeError as e:
        print(e)
    


