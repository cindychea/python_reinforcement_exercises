emotions = {
    'happiness': 2,
    'exhaustion': 3,
    'excitement': 1,
}

class Person:
    def __init__(self, name):
        self.name = name

    def degree(self):
        for emotion, value in emotions:
            if emotion == 1:
                return 'low'
            elif emotion == 2:
                return 'medium'
            elif emotion == 3:
                return 'high'
    
    def __str__(self):
        return "My name is {} and I am feeling a {} amount of {}.".format(self.name, degree(), emotion)

person1 = 'Cindy'

print(degree('Cindy'))

