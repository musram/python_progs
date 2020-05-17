#https://realpython.com/python-application-layouts/

'''
helloworld/
©¦
©À©¤©¤ bin/
©¦
©À©¤©¤ docs/
©¦   ©À©¤©¤ hello.md
©¦   ©¸©¤©¤ world.md
©¦
©À©¤©¤ helloworld/
©¦   ©À©¤©¤ __init__.py
©¦   ©À©¤©¤ runner.py
©¦   ©À©¤©¤ hello/
©¦   ©¦   ©À©¤©¤ __init__.py
©¦   ©¦   ©À©¤©¤ hello.py
©¦   ©¦   ©¸©¤©¤ helpers.py
©¦   ©¦
©¦   ©¸©¤©¤ world/
©¦       ©À©¤©¤ __init__.py
©¦       ©À©¤©¤ helpers.py
©¦       ©¸©¤©¤ world.py
©¦
©À©¤©¤ data/
©¦   ©À©¤©¤ input.csv
©¦   ©¸©¤©¤ output.xlsx
©¦
©À©¤©¤ tests/
©¦   ©À©¤©¤ hello
©¦   ©¦   ©À©¤©¤ helpers_tests.py
©¦   ©¦   ©¸©¤©¤ hello_tests.pyx
©¦   ©¦
©¦   ©¸©¤©¤ world/
©¦       ©À©¤©¤ helpers_tests.py
©¦       ©¸©¤©¤ world_tests.py
©¦
©À©¤©¤ .gitignore
©À©¤©¤ LICENSE
©¸©¤©¤ README.md
'''

'''hello/__init__.py: This file has many functions, but for our purposes it tells the Python interpreter that this directory is a package directory.
 You can set up this __init__.py file in a way that enables you to import classes and methods from the package as a whole, instead of knowing the 
internal module structure and importing from helloworld.helloworld or helloworld.helpers.
'''
