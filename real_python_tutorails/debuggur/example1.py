#https://florian-dahlitz.de/blog/how-to-debug-your-python-code
# modify.py


"""
c - Continue the execution until a new breakpoint occurs or the script finished
l - List source code around the current line
s - Execute the current line and stop at the next possible occasion
n - Like s but if the current line is a function call, the whole function is executed and not a single step inside of it
p - Evaluate the expression in the current context and print its value (pretty similar but not the same as calling print())
q - Quit from the debugger and abort the program being executed (BdbQuit is raised)
"""

import pdb

z = 2_000


def modify(x: int, y: int):
    global z
    y, z = z, y
    z += x + y


height, width = 720, 1080
pdb.set_trace()           #set a breakpoint by using the set_trace() function 
modify(height, width)
