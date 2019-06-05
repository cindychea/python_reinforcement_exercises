import inflect
# pip install inflect if not already installed
# https://pypi.org/project/inflect/

def show_indicator():
    p = inflect.engine()
    print('Please enter a number')
    user_number = int(input())
    print(p.ordinal(user_number))
show_indicator()

# Write a function that accepts a number as an argument and returns a string containing that number along with its "ordinal indicator". 
# E.g. passing in 1 would return "1st", 2 would return "2nd", 3 would return "3rd", 4 would return "4th", etc.
# Make sure your function works for every number between 1 and 20. If you're feeling ambitious, see if you can get it working for numbers beyond that.