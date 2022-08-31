# What is self in a program?
# self is a parameter in each method as a local variable
# self is a convention we use in Python (You could use any word!)
# every method's first parameter must be self and it refers to the instance we are running now
# makes scoping easier to implement and understand.
# Python rewrites the method call and the instance becomes the first argument

class Person():
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}")

p = Person('Aaron')
p.greet()