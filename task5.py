def count_word_frequencies(word_list):
    unique_words = set(word_list)
    counts = {word: 0 for word in unique_words}
    for i in unique_words:
        for j in word_list:
            if i == j:
                counts[i] += 1
    return counts

words = ["Welcome", "Ali", "Hi", "Ali", "No", "Hi", "No", "Ali", "No", "Ali"]
result = count_word_frequencies(words)
print(result)