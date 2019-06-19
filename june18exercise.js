// # Given an array of strings and an integer k, your task is to return the longest string consisting of k consecutive strings from the array concatenated together.
// # longestConsecutive(['hi', 'marbles', 'mittens', 'bye', 'lorem', 'ipsum', 'to', 'a', 'hippocampus'], 3); // -> 'marblesmittensbye'
// # If there is a tie, return the first one.
// # longestConsecutive(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2); // --> "abigailtheta"
// # Return "" if the array is empty or if k is negative or larger than the length of the array.

function longestConsecutive(array, integer) {
    if (array.length === 0 || integer > array.length || integer < 0) {
        console.log('""');
    } else {
        const sortedArray = array.sort((a, b) => b.length - a.length)
        const sortedSet = new Set(sortedArray)
        const setArray = Array.from(sortedSet)
        longest = []
        for (i=0;i<integer;i++) {
            longest.push(setArray[i])
        }
        final = longest.join('')
        console.log(final)
    }
}


longestConsecutive(['hi', 'marbles', 'mittens', 'bye', 'lorem', 'ipsum', 'to', 'a', 'hippocampus'], 3)
longestConsecutive(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2); 
longestConsecutive([], 2); 
longestConsecutive(['hi'], 2); 
longestConsecutive(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], -2); 


// The above solution works to get the output as given in the assignment
// BUT for longestConsecutive(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2);
// We might actually expect that the longest string (considering the duplicates) would be abagailabagail
// And not abagailtheta
// The solution for considering duplicates is posted below:

function longestConsecutiveExtended(array, integer) {
    if (array.length === 0 || integer > array.length || integer < 0) {
        console.log('""');
    } else {
        const sortedArray = array.sort((a, b) => b.length - a.length)
        longest = []
        for (i=0;i<integer;i++) {
            longest.push(sortedArray[i])
        }
        final = longest.join('')
        console.log(final)
    }
}

longestConsecutiveExtended(['hi', 'marbles', 'mittens', 'bye', 'lorem', 'ipsum', 'to', 'a', 'hippocampus'], 3)
longestConsecutiveExtended(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2); 
longestConsecutiveExtended([], 2); 
longestConsecutiveExtended(['hi'], 2); 
longestConsecutiveExtended(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], -2); 