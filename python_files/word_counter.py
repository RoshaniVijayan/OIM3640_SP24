# NLP 
import matplotlib.pyplot as plt
from operator import itemgetter
import os

path = "data/desolation_row.txt"

file = open(path, "r")
text = file.read()
file.close()

punc = '",.?!;'
for mark in punc:
    text = text.replace(mark, "")
split_text = text.lower().split()

counts = dict()
for word in split_text:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1    

print("{'Word':<15}{'Count':>3}")
print("-" * 18)

x = [] 
y = []
for word in sorted(counts.items(), key=itemgetter(1), reverse=True):
    if word[1] > 2:
        print(f"{word[0]:<15}{word[1]:>3}")
        x.append(word[0])
        y.append(word[1])

plt.bar(x[:10],y[:10])
plt.show()        
# print(text)
# print(f"{split_text}")
print(f"Number of words: {len(split_text)}")
print(f"Unique words: {len(set(split_text))}")
print(f"Prop. unique words: {len(set(split_text))/len(split_text):.2f}")
# print(counts)