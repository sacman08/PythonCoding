class Dog:
    """ A simple attempt model a dog using classes."""
    
    def __init__(self, name, age):
        """Init the name and attribute."""
        self.name = name
        self.age = age
        
    def sit(self):
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        print(f"{self.name} rolled over!")
        
        
class Restaurant:
    """ Example 9 from Crash Course"""
    def __init__(self, name, rtype, status):
        self.name = name
        self.rtype = rtype
        self.status = status
        
    def describe_restaurant(self):
        print(f'The resturant name is {self.name} and our cuisine is {self.rtype}.')
        
    def open_restaurant(self):
        print(f'{self.name} is {self.status} for business!')
    

my_restaurant = Restaurant('The Juicy Burritto', 'Mexican', 'Open')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

""" Instance for dog class (remove triple quotes to use)"""
my_dog = Dog('Woofie', 9)
your_dog = Dog('Janelle', 15)


print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f'\nYour dog\'s name is {your_dog.name}.')
print(f'Your dog is {your_dog.age} years old.')
your_dog.sit()
