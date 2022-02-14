with open("filter.txt", "r") as file:
    words = file.read().splitlines()

words_valid = filter(lambda x: x.strip(), words)
words_valid = map(lambda x: x.strip().lower(), words_valid)
words_valid = sorted(set(words_valid))

with open("filter.txt", "w") as file:
    file.write("\n".join(words_valid))
