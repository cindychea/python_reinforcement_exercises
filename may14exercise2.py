# Pick three names and store them in a list.
# Prompt the user to enter their name. If their name is one of the names in the list, display a greeting message that includes their name. If their name isn't in the list, display "Who goes there?"

selected_names = ['Sofia', 'Elizabeth', 'Christine']

def greeting_or_not():
    print('Please enter your name.')
    user_name = input()
    if user_name == selected_names[0]:
        return "Hi Sofia, hope you have a great day!"
    elif user_name == selected_names[1]:
        return "Hi Elizabeth, hope you have a great day!"
    elif user_name == selected_names[2]:
        return "Hi Christine, hope you have a great day!"
    else: 
        return "Who goes there?"

print(greeting_or_not())