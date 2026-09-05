sentence1 = input()
sentence2 = input()

words1 = sentence1.split()
words2 = sentence2.split()

common_words = []

for word in words1:
    if word in words2 and word not in common_words:
        common_words.append(word)

print("Common words:")

for word in common_words:
    print(word)
    