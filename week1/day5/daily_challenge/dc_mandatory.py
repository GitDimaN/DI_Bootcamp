words = input("comma-separated words, no spaces: \n").split(",")
print(",".join(sorted(words)))


def longest_word(sentence):
    words = sentence.split()
    if not words:
        return ""

    longest = words[0]
    for word in words[1:]:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word("A thing of beauty is a joy forever."))