def count_letters(word):
    letter_count = {}
    for letter in word:
        if letter.isalpha():  # Ensure the character is a letter
            letter = letter.lower()  # Convert to lowercase for case insensitivity
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

# Example usage
word = input("Enter a word: ")
print(count_letters(word))