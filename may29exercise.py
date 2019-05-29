seating_chart = [
    [None, "Pumpkin", None, None],
    ["Socks", None, "Mimi", None],      # changed nil to none
    ["Gismo", "Shadow", None, None],
    ["Smokey","Toast","Pacha","Mau"]
]

# Display the list of available seats to your user
i = 0
for row in seating_chart:
    i += 1
    n = 0
    for seat in row:
        n += 1
        if seat == None:
            print(f'Row {i} seat {n} is free.')

# For each available seat, use input() to prompt your user to choose whether they want to claim that spot. 
# If they indicate they want to claim a seat, prompt them for their name and insert it into the array to show that they've been seated, like so:
def seat_picker():
    i = 0
    for row in seating_chart:
        i += 1
        n = 0
        for seat in row:
            n += 1
            if seat == None:
                print(f'Row {i} seat {n} is free. Do you want to sit there? (y/n)')
                decision = input()
                if decision == 'y':
                    print('What is your name?')
                    name = input()
                    del seating_chart[i-1][n-1]
                    seating_chart[i-1].insert(n-1, name)
                    print(f'Please take your seat in row {i} seat {n}.')
                    return
                else:
                    pass
seat_picker()

print(seating_chart)
