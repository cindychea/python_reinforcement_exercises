emotions = {
    'happiness': 2,
    'exhaustion': 3,
    'excitement': 1,
}

class Person:
    def __init__(self, name, emotions):
        self.name = name
        self.emotions = emotions

    def __str__(self):
        return "My name is {} and I am feeling {}".format(self.name, emotions)

    def degree(self):
        for emotion, value in self.emotions.items():
            if value == 1:
                print('I am feeling a low amount of {}.'.format(emotion))
            elif value == 2:
                print('I am feeling a medium amount of {}.'.format(emotion))
            elif value == 3:
                print('I am feeling a high amount of {}.'.format(emotion))

person1 = Person('Cindy', emotions)
print(person1)
person1.degree()
