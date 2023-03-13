# Print Upper Words 
def print_upper_words(words):

    for word in words:
        print(word.upper())

# Print Upper Words 2
def print_upper_words2(words):

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

# Print Upper Words 3
def print_upper_words3(words, must_start_with):
    for word in words:
        for x in must_start_with:
            if word.startswith(x):
                print(word.upper())
                break

