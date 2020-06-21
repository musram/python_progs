#https://florian-dahlitz.de/blog/how-to-debug-your-python-code



# div.py


def div(dividend: int = 1, divisor: int = 0) -> float:
    return dividend / divisor


"""
use postmortem pdb
   in repl
       import pdb
       import example2.py
       example2.div()
       pdb.pm()
