# How do you list the functions in a module?
import random

# lets import a random module(get it?)

list_functions = [one_attrname
                  for one_attrname in dir(random)
                  if type(getattr(random, one_attrname)) == type(random.randint)]

print(list_functions)
