# Sometimes we want to change a variable to a different type. This is called casting

# Here, we want the user to input two numbers in order to add them. We need to convert them to numbers, as
# user input comes in the form of a string

print("Enter a number")
a_string = input()

print("Enter another number")
b_string = input()

# This is the important part, we are casting strings to floats!
a = float(a_string)
b = float(b_string)

# Try replacing this line with `sum = a_string + b_string`. What will happen?
sum = a + b

print("The sum of those numbers is " + str(sum))