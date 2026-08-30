text = input("Write a sentence: ")


def count_characters(text):

    count_characters = len(text)
    return count_characters

def count_words(text):

    words = text.split()
    count_words = len(words)
    return count_words

def find_longest_word(text):

    words = text.split()
    longest_word = ""

    for word in words:

        if len(word) > len(longest_word):
            longest_word = word
        
    return longest_word


def count_letter_a(text):

    a = "a"
    count = 0
    text = text.lower()

    for letter in text:

        if letter == a:
            count += 1

    return count
    

characters = count_characters(text)
words = count_words(text)
longest = find_longest_word(text)
letter_a = count_letter_a(text)

print(f"Characters: {characters}")
print(f"Words: {words}")
print(f"Longest word: {longest}")
print(f"Letter 'a': {letter_a}")