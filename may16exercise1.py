# Exercise 1
# Create a Task class with a description and due_date (both strings). 
# Define an __init__ method, then try creating three instances of this class.

class Task:
    
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        
    def __repr__(self):
        return f'{self.description} by {self.due_date}'

task1 = Task('Buy Groceries', 'June 1')
task2 = Task('Clean Room', 'June 2')
task3 = Task('Visit Parents', 'June 3')

print(task1)
print(task2)
print(task3)

