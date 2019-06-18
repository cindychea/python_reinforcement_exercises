# Create a Location class with a name.
class Location:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# Create a Trip class with a list of Location instances (called stops or destinations or something similar). 
# Define a method that lets you add locations to the trip's list of destinations.
# Define a method in the Trip class that iterates through the list of locations and prints something similar to the following:
# "Began trip."
# "Travelled from Toronto to Ottawa."
# "Travelled from Ottawa to Montreal."
# "Travelled from Montreal to Quebec City."
# "Travelled from Quebec City to Halifax."
# "Travelled from Halifax to St. John's."
# "Ended trip."
class Trip:

    def __init__(self):
        self.destinations = []

    def add_location(self, location):
        self.destinations.append(location)
    
    def trip_summary(self):
        i = 0
        print('Began trip.')
        for i in range(len(self.destinations) - 1):
            print(f'Travelled from {self.destinations[i]} to {self.destinations[i+1]}.')
            i += 1
        print('Ended trip.')

# Make several instances of Locations and add them to an instance of Trip.
toronto = Location('Toronto')
ottawa = Location('Ottawa')
montreal = Location('Montreal')
quebec_city = Location('Quebec City')
halifax = Location('Halifax')
st_johns = Location("St John's")
my_trip = Trip()

my_trip.add_location(toronto)
my_trip.add_location(ottawa)
my_trip.add_location(montreal)
my_trip.add_location(quebec_city)
my_trip.add_location(halifax)
my_trip.add_location(st_johns)

my_trip.trip_summary()