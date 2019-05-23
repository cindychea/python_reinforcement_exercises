def word_counter():
    print("Please enter a string to get the word count.")
    user_string = input()
    words = user_string.split()
    word_count = len(words)
    print(f'The number of words is {word_count}.')

word_counter()