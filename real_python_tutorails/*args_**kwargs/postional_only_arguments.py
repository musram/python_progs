#https://realpython.com/lessons/positional-only-arguments/










if __name__ == "__main__":

   print(help(float))


   """
   Look closely at the signature of float(). Notice the slash (/) after the parameter. What does it mean?

It turns out that while the one parameter of float() is called x, youre not allowed to use its name
   """
   try:
      print(float(x="3.8"))
   except TypeError as e:
      print(e)

   """
   In Python 3.8, you can use / to denote that all arguments before it must be specified by position. 
   """

   def incr(x, /):
      return x +1

   print(incr(3.2))

   try:

      print(incr(x=3.2))
   except TypeError as e:
      print(e)

   """
   By adding / after x, you specify that x is a positional-only argument. You can combine regular arguments with positional-only ones by placing the regular arguments after the slash
x   """

   """
   In greet(), the slash is placed between name and greeting. This means that name is a positional-only argument, while greeting is a regular argument that can be passed either by position or by keyword.
   """
   
   def greet(name, /, greeting="Hello"):
      return f"{greeting}, {name}"

   print(greet("sai"))

   print(greet("sai", greeting="stupid job"))

   try:
      print(greet(name="sai", greeting="stupid job"))
   except TypeError as e:
      print(e)


   """
   Positional-only arguments nicely complement keyword-only arguments. In any version of Python 3, you can specify keyword-only arguments using the star (*). Any argument after * must be specified using a keyword
   """

   def to_fahrenheit(*, celsius):
      return 32 + celsius * 9 / 5


   try:
      print(to_fahrenheit(40))
   except TypeError as e:
      print(e)


   print(to_fahrenheit(celsius=40))


   def print_greeting(name, *, use_colors=False):
      return f"{name} coloures {use_colors}"

   print(print_greeting(name="sai"))

   print(print_greeting(name="sai", use_colors=True))

   try:
      print(print_greeting("sai", True))
   except TypeError as e:
      print(e)

   try:
      print(print_greeting(use_colors=True))
   except TypeError as e:
      print(e)
   

   """
   You can combine positional-only, regular, and keyword-only arguments by specifying them in this order separated by / and *. In the following example, text is a positional-only argument, border is a regular argument with a default value, and width is a keyword-only argument with a default value:
   """
   def headline(text, /, border="~", *, width=50):
      return f" {text} ".center(width, border)

   print(headline("Positional-only Arguments"))

   try:
      headline(text="Positional-only Arguments")

   except TypeError as e:
      print(e)

   print(headline("Python 3.8", "="))

   print(headline("Python 3.8", border="="))

   print(headline("Python", "@", width=38))

   try:
      print(headline("Python", "@", 38))

   except TypeError as e:
      print(e)
      

