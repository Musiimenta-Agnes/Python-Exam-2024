# Define the function name

def numbers():
    number1 = int(input("Enter the first number of your choice: "))
    number2 = int(input("Enter the second number of your choice:"))
    

    return number1 + number2, number1 - number2, number1 ** number2

# Create a variable to hold your values
number = numbers()

print(f" The sum, difference, and quotient of the numbers are {number} respectively")
    
 






















