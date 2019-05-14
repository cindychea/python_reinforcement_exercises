# Define a function that accepts a list of numbers as an argument and returns the sum of the odd numbers in the list.

def number_list(numbers):
    sum = 0
    for number in numbers:
        if number % 2 != 0:
            sum += number
        else:
            continue
    return sum

print(number_list([34, 22, 13, 5]))