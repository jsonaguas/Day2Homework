#Task 1
response = input('Enter a number:')
user_number = int(response)

if user_number > 0:
    print("The number is positive.")
elif user_number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


#=====================
#Task 2
number1 = input('Enter 1st number ')
number_one=int(number1)
number2 = input('Enter 2nd number ')
number_two=int(number2)
number3 = input('Enter 3rd number ')
number_three=int(number3)

if number_one > number_two and number_one > number_three:
    print("The largest number is ", number_one)
elif number_two > number_one and number_two > number_three:
    print("The largest number is ", number_two)
elif number_three > number_one and number_three > number_two:
    print("The largest number is ", number_three)