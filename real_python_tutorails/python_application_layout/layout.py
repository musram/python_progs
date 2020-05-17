#https://realpython.com/python-application-layouts/

'''
helloworld/
��
������ bin/
��
������ docs/
��   ������ hello.md
��   ������ world.md
��
������ helloworld/
��   ������ __init__.py
��   ������ runner.py
��   ������ hello/
��   ��   ������ __init__.py
��   ��   ������ hello.py
��   ��   ������ helpers.py
��   ��
��   ������ world/
��       ������ __init__.py
��       ������ helpers.py
��       ������ world.py
��
������ data/
��   ������ input.csv
��   ������ output.xlsx
��
������ tests/
��   ������ hello
��   ��   ������ helpers_tests.py
��   ��   ������ hello_tests.pyx
��   ��
��   ������ world/
��       ������ helpers_tests.py
��       ������ world_tests.py
��
������ .gitignore
������ LICENSE
������ README.md
'''

'''hello/__init__.py: This file has many functions, but for our purposes it tells the Python interpreter that this directory is a package directory.
 You can set up this __init__.py file in a way that enables you to import classes and methods from the package as a whole, instead of knowing the 
internal module structure and importing from helloworld.helloworld or helloworld.helpers.
'''
