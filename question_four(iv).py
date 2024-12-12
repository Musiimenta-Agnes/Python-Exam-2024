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