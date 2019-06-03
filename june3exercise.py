# Write code to generate a dictionary where the keys are the numbers from 1 to 50 and the values follow these rules:
    # if the number is divisible by 2 the value should be one more than the key
    # if the number is divisible by 7 the value should be one less than the key
    # if the number is divisible by 2 and 7 the value should be the key multiplied by 2
    # otherwise the value should be the same number as the key

dictionary = {}

for number in range(1,51):
    if number % 2 == 0 and number % 7 == 0:
        dictionary[number] = number * 2
    elif number % 2 == 0:
        dictionary[number] = number + 1
    elif number % 7 == 0:
        dictionary[number] = number - 1
    else:
        dictionary[number] = number
print(dictionary)


