word = input("Enter a word or number: ")
def is_palindrome(word):
    word = word.lower()
    reversed_word = word[::-1]
    if word == reversed_word:
        print("PALINDROME!")
    else:
        print("NOT A PALINDROME")

is_palindrome(word)