import random
import nltk
from nltk.tokenize import word_tokenize

# Sample training text
text = "the cat sat on the mat and the dog lay on the rug"

# Tokenize the text
tokens = word_tokenize(text)

# Build bigram model: {(w1): [w2,...], ...}
bigrams = {}
for i in range(len(tokens)-1):
    w1, w2 = tokens[i], tokens[i+1]
    bigrams.setdefault(w1, []).append(w2)

# Function to generate text using the bigram model
def generate_text(bigrams, start_word, length=10):
    result = [start_word]
    current_word = start_word
    for _ in range(length-1):
        next_words = bigrams.get(current_word)
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
        current_word = next_word
    return ' '.join(result)

# Generate and print a sample sentence
print(generate_text(bigrams, 'the', 10))

#--------------------OUTPUT---------------------------

C:\Users\HP\OneDrive\Desktop\NLP Programs>python 6_Basic_Programs.py
the dog lay on the rug