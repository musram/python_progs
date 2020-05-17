class ComputerState(object):

   name = "state"
   allowed = []

   def switch(self, state):
      """ Switch to new state """
      if state.name in self.allowed:
         print('Current:',self,' => switched to new state',state.name)
         self.__class__ = state
      else:
         print('Current:',self,' => switching to',state.name,'not possible.')

   def __str__(self):
      return self.name



class off(ComputerState):
    name = "off"
    allowed = ['on']

class on(ComputerState):
    name = 'on'
    allowed = ['on', 'suspend',  'hibernate']

class suspend(ComputerState):
    name = 'suspend'
    allowed = ['on']

class hibernate(ComputerState):
    name = 'hibernate'
    allowed = [ 'on']

class Computer(object):
   """ A class representing a computer """
   
   def __init__(self, model='HP'):
      self.model = model
      # State of the computer - default is off.
      self.state = off()
   
   def change(self, state):
      """ Change state """
      self.state.switch(state)

if __name__ == "__main__":
   comp = Computer()
   comp.change(on)
   comp.change(off)
   comp.change(on)
   comp.change(suspend)
   comp.change(hibernate)
   comp.change(on)
   comp.change(off)    
