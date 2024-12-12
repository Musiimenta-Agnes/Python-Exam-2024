

# (i)

# Defining a function name

def student_details():
    student_name = 'Gloria Arinda'
    student_number = 'SEP23/DSC/088U/F'
    programming = 90
    data_science = 87
    computer_applications = 77

# Performing the formular of average
    average_mark = programming + data_science + computer_applications / 3
    print(f" The average mark of the student is: {average_mark:.3f}")

student_details()







# (ii)


# Defining a function name

def car_miles():
    miles_driven = int(input("Enter the number of miles driven: "))
    gallons_of_gas_used = int(input("Enter the number of gallons used: "))

# Applying the formular given

    miles_per_gallons = miles_driven / gallons_of_gas_used

    print(f" The cars miles per gallon used are: {miles_per_gallons}")

car_miles()








# (iii)

# Defining the function name 

def odd_numbers():
    for numbers in range(1,101):
        if numbers %2 != 0:
         print(f" {numbers}")


odd_numbers()