# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = input("Enter first word: ")
    anagram = input("Enter second word: ")

    sorted_word = sorted(word)
    sorted_anagram = sorted(anagram)

    if (sorted_word == sorted_anagram):
        print('True')
    else:
        print('False')


find_anagram("hello", "check")
