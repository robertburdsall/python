# Module = a file containing python code. Could contain functions, classes, etc.
# used with modular programming - an easy way to separate programs into parts

import messages as msg  # changes the name of the module to something you can specify right here
from messages import hello, bye  # imports the functions directly
#  from messages import * # imports all functions from this module - not recommended on large projects

# how to call a function from a different module - (name of module).(name of function in module)

 
hello()
bye()
