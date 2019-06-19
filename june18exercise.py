# Given an array of strings and an integer k, your task is to return the longest string consisting of k consecutive strings from the array concatenated together.
# longestConsecutive(['hi', 'marbles', 'mittens', 'bye', 'lorem', 'ipsum', 'to', 'a', 'hippocampus'], 3); // -> 'marblesmittensbye'
# If there is a tie, return the first one.
# longestConsecutive(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2); // --> "abigailtheta"
# Return "" if the array is empty or if k is negative or larger than the length of the array.


def longestConsecutive(array, integer):
    if array == [] or integer > len(array) or integer < 0:
        print('""')
    else:
        words_and_lengths = []
        # if you do not want duplicates concatenated (only unique words)
        for word in set(array):
        # if you are okay with duplicates being concatenated
        # for word in array:
            words_and_lengths.append({'word': word, 'length': len(word)})
        ordered_words_and_lengths = sorted(words_and_lengths, key=lambda k: k['length'], reverse=True)
        longest_words = ordered_words_and_lengths[0:integer]
        top_words = []
        for item in longest_words:
            top_words.append(item['word'])
        print(''.join(top_words))


longestConsecutive(['hi', 'marbles', 'mittens', 'bye', 'lorem', 'ipsum', 'to', 'a', 'hippocampus'], 3)

# with this example, the longest consecutive string would be abagailabagail unless we only want unique values
# this is why there is an option for either line 14 or line 16 above
longestConsecutive(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2); 

longestConsecutive([], 2); 

longestConsecutive(['hi'], 2); 

longestConsecutive(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], -2); 
