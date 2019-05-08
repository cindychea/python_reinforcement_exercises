# Define a function that accepts a percentage as an argument and returns a letter grade (A+, A, A-, B+, etc) for that percentage.
# Prompt your user to enter a percentage and display a message showing them the equivalent letter grade.

def letter_grade():
    print("What was your grade as a percentage?")
    percent_grade = input()
    if int(percent_grade) >= 95:
        return 'A+'
    elif int(percent_grade) >= 87:
        return 'A'
    elif int(percent_grade) >= 80:
        return 'A-'
    elif int(percent_grade) >= 77:
        return 'B+'
    elif int(percent_grade) >= 73:
        return 'B'
    elif int(percent_grade) >= 70:
        return 'B-'
    elif int(percent_grade) >= 67:
        return 'C+'
    elif int(percent_grade) >= 63:
        return 'C'
    elif int(percent_grade) >= 60:
        return 'C-'
    elif int(percent_grade) >= 57:
        return 'D+'
    elif int(percent_grade) >= 53:
        return 'D'
    elif int(percent_grade) >= 50:
        return 'D-'
    else: 
        return 'F'
print("Your letter grade is {}.".format(letter_grade()))

