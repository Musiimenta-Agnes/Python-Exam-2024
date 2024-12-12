# Finding the sum of only odd numbers from the given list.

integers = [4,7,2,9,12,15]
sum_odd_numbers = 0
for number in integers:
    if number %2 !=0:
        sum_odd_numbers+=number
print(f"The sum of all odd numbers is {sum_odd_numbers}")
