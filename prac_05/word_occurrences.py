"""
Word Occurrences
Estimate: 15 minutes
Actual:   17 minutes
"""
text = input("Enter a text: ").lower()
words = text.split()
word_count = {}
# Count the occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
sorted_word = dict(sorted(word_count.items()))
max_word_length = max(len(word) for word in sorted_word)
print("\nWord occurrences:")
for word, count in sorted_word.items():
    print(f"{word:{max_word_length}} : {count}")