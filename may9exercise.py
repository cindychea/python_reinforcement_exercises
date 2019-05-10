# list_trains = [
# {'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
# {'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
# {'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
# {'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
# {'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
# {'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
# {'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
# {'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
# ]

# train111_direction = list_trains[7]['direction']
# print(train111_direction)

# train80B_frequency = list_trains[5]['frequency_in_minutes']
# print(train80B_frequency)

# train610_direction = list_trains[2]['direction']
# print(train610_direction)

# north_trains = []
# for train in list_trains:
#     if train['direction'] == 'north':
#         print(train['train'])

# east_trains = []
# for train in list_trains:
#     if train['direction'] == 'east':
#         print(train['train'])

# def direction():
#     print('Which direction are you going?')
#     train_dir = input()
#     for train in list_trains:
#         if train['direction'] == train_dir:
#             print(train['train'])
# direction()
# OR WITHOUT QUESTION/PROMPT:
# def direction(train_dir):
#     for train in list_trains:
#         if train['direction'] == train_dir:
#             print(train['train'])
# direction('north')
# direction('east')

# list_trains[1]['first_departure_time'] = '6'
# print(list_trains[1])

trains = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

trains_by_frequency = {}
for train in trains:
    freq = train['frequency_in_minutes']
    name = train['train']
    if freq in trains_by_frequency:
        trains_by_frequency[freq].append(name)
    else:
        trains_by_frequency[freq] = [name]
print(trains_by_frequency)