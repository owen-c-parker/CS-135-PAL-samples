# There's one bug lurking...

print("How many days are there until your birthday?")
days = int(input())

if days > 30:
    message = "It's nowhere near your birthday"
elif days > 5:
    message = "Not long now"
elif days > 0:
    message = "I bet your friends are planning a party"
elif days = 0:
    message = "Happy birthday!"
else:
    message = "It seems your birthday has passed"

print(message)