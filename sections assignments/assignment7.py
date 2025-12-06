sentences = [
    "Hello world",
    "Goodbye world",
    "But people can go, from people you know, to people you don't",
]

lengths = list(map(lambda sentence: list(map(len, sentence.split())),sentences))

print("Sentences: ", sentences)
print("lengths: ", lengths)