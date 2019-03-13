def break_words(words):
    """This function will break up words for us"""
    return words.split(' ')

def sort_words(words):
    """This function will sort up words for us"""
    return sorted(words)

def print_first_word(words):
    """Print the first word for us after popping it up"""
    print(words.pop(0))

def print_last_word(words):
    """Print the last word for us after popping it up"""
    print(words.pop(-1))

def sort_sentence(sentence):
    """Take the full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Print the first and last word of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Print the first and last word of the sentence after sort it up"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    