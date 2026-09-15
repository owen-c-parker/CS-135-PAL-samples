# The comparison of an if statement doesn't need to be evaluated then and there, it can be a boolean
# variable instead

value = 3 > 2
# We could also say:
#   value = True

if value:
    print("It's true!")