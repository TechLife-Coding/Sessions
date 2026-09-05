text = input('Type: ')

words = text.split()

most_common = words[0]
max_count = words.count(words[0])

for word in words:
    count = words.count(word)

    if count > max_count:
        max_count = count
        most_common = word

print(most_common, "->", max_count)
