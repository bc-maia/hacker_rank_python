from pprint import pprint

book_title = [
    "great",
    "expectations",
    "the",
    "adventures",
    "of",
    "sherlock",
    "holmes",
    "the",
    "great",
    "gasby",
    "hamlet",
    "adventures",
    "of",
    "huckleberry",
    "fin",
]


# TODO: second way of word counting using conditionals
word_counter = {}
for word in book_title:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1
pprint(word_counter)


# TODO: first way of word counting using built-in get
word_counter = {}
for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1
pprint(word_counter)
