# Exercise 2
# Create a TodoList class with a tasks list (which will contain instances of the Task class). 
# Create an __init__ method and an add_task method that allows you to pass in an instance of your Task class. 
# Try creating a todo list and adding your three tasks to it.

from may16exercise1 import *

class TodoList:

    def __init__(self, name):
        self.name = name
        self.tasks_list = []

    def __str__(self):
        for task in self.tasks_list:
            return f'{task.description}, {task.due_date}'
            # print(f'{task.description}, {task.due_date}')

    def add_task(self, task):
        self.tasks_list.append(task)

my_list = TodoList('My Todo List')
my_list.add_task(task1)
my_list.add_task(task2)
my_list.add_task(task3)

print(my_list.tasks_list)
print(my_list)
print(type(f'{task1.description}, {task1.due_date}'))