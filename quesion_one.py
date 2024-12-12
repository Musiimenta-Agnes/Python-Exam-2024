
#(i)
# Define a function name
def circle_area(radius):
    area = 3.14 * radius **2
    return area

# Create a variable to hold the values
the_area = circle_area(4)

print(f"The area of a circle of radius 4 is {the_area}")



# (ii)
# Finding the sum of only odd numbers from the given list.

integers = [4,7,2,9,12,15]
sum_odd_numbers = 0
for number in integers:
    if number %2 !=0:
        sum_odd_numbers+=number
print(f"The sum of all odd numbers is {sum_odd_numbers}")



   # (iii) 

    # Define the function name

def numbers():
    number1 = int(input("Enter the first number of your choice: "))
    number2 = int(input("Enter the second number of your choice:"))
    

    return number1 + number2, number1 - number2, number1 ** number2

# Create a variable to hold your values
number = numbers()

print(f" The sum, difference, and quotient of the numbers are {number} respectively")




# (v)

# The student information

student_info = {
    'name': 'Alice',
    'age': 20,
    'grade': 'A'
}
# Updating age to 26
student_info['age'] = 26

# Adding the key value pair
student_info['city'] = 'Kampala'

print(F"The new updated dictionary is {student_info}") 