// Create a Location class with a name.

class Location {
    constructor(name) {
        this.name = name;
    }
}

// Create a Trip class with a list of Location instances (called stops or destinations or something similar). 
// Define a method that lets you add locations to the trip's list of destinations.
// Define a method in the Trip class that iterates through the list of locations and prints something similar to the following:
// "Began trip."
// "Travelled from Toronto to Ottawa."
// "Travelled from Ottawa to Montreal."
// "Travelled from Montreal to Quebec City."
// "Travelled from Quebec City to Halifax."
// "Travelled from Halifax to St. John's."
// "Ended trip."

class Trip {
    constructor() {
        this.destinations = []
    }

    addLocation(location) {
        this.destinations.push(location);
    }

    tripSummary() {
        var i;
        console.log('Began trip.')
        for (i=0; i<(this.destinations.length - 1); i++) {
            console.log('Travelled from ' + this.destinations[i].name + ' to ' + this.destinations[i+1].name + '.')
        }
        console.log('Ended trip.')
    }
}

// Make several instances of Locations and add them to an instance of Trip.
const toronto = new Location('Toronto')
const ottawa = new Location('Ottawa')
const montreal = new Location('Montreal')
const quebecCity = new Location('Quebec City')
const halifax = new Location('Halifax')
const stJohns = new Location("St John's")
myTrip = new Trip()

myTrip.addLocation(toronto)
myTrip.addLocation(ottawa)
myTrip.addLocation(montreal)
myTrip.addLocation(quebecCity)
myTrip.addLocation(halifax)
myTrip.addLocation(stJohns)

myTrip.tripSummary()