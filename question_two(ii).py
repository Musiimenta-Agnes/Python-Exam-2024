
# Defining a function name

def car_miles():
    miles_driven = int(input("Enter the number of miles driven: "))
    gallons_of_gas_used = int(input("Enter the number of gallons used: "))

# Applying the formular given

    miles_per_gallons = miles_driven / gallons_of_gas_used

    print(f" The cars miles per gallon used are: {miles_per_gallons}")

car_miles()
