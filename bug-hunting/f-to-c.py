# There's one mistake hiding in this program...

print("Enter a temperature in Fahrenheit")
fahrenheit = input()

celcius = (fahrenheit - 32) * (5 / 9) # The formula is correct, that's not the mistake :)

print(f"The temperature in Celcius is ${celcius} degrees")