def sort_words_by_length(sentence):
    words = sentence.split()
    return " ".join(sorted(words, key=len))
sentence = input("Enter sentence: ")
print("Sorted by length:", sort_words_by_length(sentence))
