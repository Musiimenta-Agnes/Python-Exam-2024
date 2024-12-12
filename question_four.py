
# (i)(a)
# Object Oriented Programming (OOP) refers to the method in programming that is 
# used to perfom various programs at the sme time.






# (i)(b)
# A class in OOP is an container that handles all the attributes tha are to be included during a program.

# This differes from an object because an object stores values but a class stores attributes.






# (ii)
# Stating the sentence
sentence = 'My name is Agnes'

for word in sentence:
    print(word)






#(iii)
    #Finding the sum of two numbers

def sum_numbers(a,b):
    return a + b

# Creating a variable to store the numbers
sum = sum_numbers(3,4)

print(f" The sum of a and b is {sum}")






# (iv)
# Creating a class function

class Car:
    def __init__ (self,brand,name,color):
        self.name = name
        self.brand = brand
        self.color = color

        # Instantiating an object


car_object = Car('Toyota', 'My Car', 'Brown')

# Printing the attributes

print(f"The car brand is: {car_object.brand}")
print(f"The car name is: {car_object.name}")
print(f"The car color is: {car_object.color}")






#(v)

 # The class Car
        
class Car:
   def __init__(self,brand,name,color):
      self.brand = brand
      self.name = name
      self.color = color

# Adding a method.

def start_engine(self):
   print(f"The engine of the car has started")

   # Creating an instance  of Car and calling the method
cars = Car("Toyota", "My car","Brown")   
start_engine('self')