#https://rednafi.github.io/digressions/python/2020/03/26/python-contextmanager.html
class CustomFileOpen:
    def __init__(self, filename,mode):
        self.filename = filename
        self.mode = mode


    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, *args):
        self.file.close()


#using generator

'''
@contextmanager
def some_generator(<arguments>):
    <setup>
    try:
        yield <value>
    finally:
        <cleanup>

with some_generator(<arguments>) as <variable>:
    <body>

<setup>
try:
    <variable> = <value>
    <body>
finally:
    <cleanup>

'''


from contextlib import contextmanager

@contextmanager
def CustomFileOpenB(filename, mode):
    f = open(filename, mode)

    try:
        yield f

    finally:
        f.close()



#context  manager as decorator

from contextlib import ContextDecorator
from time import time

class RunTime(ContextDecorator):

    def __init__(self, description):
        self.description = description

    def __enter__(self):
        print(self.description)
        self.start_time = time()

    def __exit__(self, *args):
        self.end_time= time()
        run_time = self.end_time - self.start_time
        print('the function took {} sec to run'.format(run_time))


#the same can also be create the same decorator via contextlib.contextmanager decorator.

from contextlib import contextmanager

@contextmanager
def runtime(description):
    print(description)

    start_time = time()
    try:
        yield

    finally:
        end_time = time()
        run_time = end_time - start_time
        print('the function took {} sec to run'.format(run_time))


#multiple contextmanager

from contextlib import contextmanager


@contextmanager
def get_state(name):
    print("entering:", name)
    yield name
    print("exiting :", name)


#combining multiple contextmanager


from contextlib import contextmanager


@contextmanager
def a(name):
    print("entering a:", name)
    yield name
    print("exiting a:", name)


@contextmanager
def b(name):
    print("entering b:", name)
    yield name
    print("exiting b:", name)


@contextmanager
def ab(a, b):
    with a("A") as A, b("B") as B:
        yield (A, B)    

        
if __name__ == "__main__":
    with CustomFileOpenB('/etc/passwd', 'r') as f:
        print(f.readlines())


    @RunTime('This function opens a file')
    def custom_file_reader(filename, mode):
        with open(filename, mode) as f:
             print(f.readlines())

    
    print(custom_file_reader('/etc/passwd', 'r'))


    # multiple get_state can be nested like this
    with get_state("A") as A, get_state("B") as B, get_state("C") as C:
        print("inside with statement:", A, B, C)


    #combinig multiple contextmanager
    with ab(a, b) as AB:
        print("Inside the composite context manager:", AB)
    



    


        
