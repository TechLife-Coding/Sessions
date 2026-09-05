words = ["hack", "fraud", "scam", "password", "attack"]

text = input().lower()

for word in words:
    count = text.split().count(word)

    if count > 0:
        print(word, "->", count)
        