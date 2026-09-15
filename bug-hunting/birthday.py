print("How many days are there until your birthday?")
days = int(input())

message = None

if days > 100:
    message = "It's nowhere near your birthday!"
elif days > 30:
    message = "Your day is coming up!"
elif days > 5:
    message = "I bet your friends are planning a party!"
elif days = 0:
    message = "Happy birthday!"
else:
    message = "It seems your birthday has passed!"

print(message)