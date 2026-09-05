text = input('Type: ')

words = text.split()

total_characters = len(text)
total_words = len(words)

total_letters = 0
total_digits = 0
total_spaces = 0
total_uppercase = 0
total_lowercase = 0

for char in text:
    if char.isalpha():
        total_letters += 1

    if char.isdigit():
        total_digits += 1

    if char == " ":
        total_spaces += 1

    if char.isupper():
        total_uppercase += 1

    if char.islower():
        total_lowercase += 1

longest_word = words[0]
shortest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

    if len(word) < len(shortest_word):
        shortest_word = word

most_repeated_character = max(set(text), key=text.count)
most_repeated_word = max(set(words), key=words.count)

print("Total characters:", total_characters)
print("Total words:", total_words)
print("Total letters:", total_letters)
print("Total digits:", total_digits)
print("Total spaces:", total_spaces)
print("Total uppercase:", total_uppercase)
print("Total lowercase:", total_lowercase)
print("Longest word:", longest_word)
print("Shortest word:", shortest_word)
print("Most repeated character:", most_repeated_character)
print("Most repeated word:", most_repeated_word)
