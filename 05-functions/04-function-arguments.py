
#When defining a function, you can define values that can change the output or functionality of the function.
#These are called parameters.
def calculate_area(length, width):
    return length * width

#The numbers we are passing into this function call are called arguments.
area = calculate_area(10, 20)
print(area)