from collections import Counter
with open("data.txt","r") as f:
    text=f.read()
words=text.split()
print(f"Number of words in the file:{len(words)}")
word_counts=Counter(words)
print("Frequency of each word:", word_counts)
print("The 5 most frequently occurring words:", word_counts.most_common(5))