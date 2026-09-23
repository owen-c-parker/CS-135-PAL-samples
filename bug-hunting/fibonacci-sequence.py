numbers = [0, 1]

index = 1

while index < 50:
    numbers.append(numbers[index] + numbers[index + 1])
    print(numbers[index - 1])