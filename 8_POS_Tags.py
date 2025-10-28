import random

# Example training corpus (word, POS tag)
training_data = [
    ('The', 'DT'), ('cat', 'NN'), ('sat', 'VBD'), ('on', 'IN'), ('the', 'DT'),
    ('mat', 'NN'), ('and', 'CC'), ('dog', 'NN'), ('lay', 'VBD'), ('rug', 'NN')
]

# Build a frequency table: {word: {tag: count, ...}, ...}
freq_table = {}
for word, tag in training_data:
    freq_table.setdefault(word.lower(), {})
    freq_table[word.lower()][tag] = freq_table[word.lower()].get(tag, 0) + 1

# For each word, compute probabilities and select highest (stochastic if tied)
def stochastic_pos_tag(sentence, freq_table, default_tag='NN'):
    tokens = sentence.split()
    tags = []
    for word in tokens:
        word_lower = word.lower()
        if word_lower in freq_table:
            tag_counts = freq_table[word_lower]
            max_count = max(tag_counts.values())
            # Tags tied for max probability
            candidates = [tag for tag, count in tag_counts.items() if count == max_count]
            chosen_tag = random.choice(candidates)
        else:
            chosen_tag = default_tag  # Unknown word: default to 'NN'
        tags.append((word, chosen_tag))
    return tags

# Test sentence
test_sentence = "The dog sat on the rug"
tags = stochastic_pos_tag(test_sentence, freq_table)
print("POS Tags:", tags)

#------------------------------OUTPUT----------------------------------------

C:\Users\HP\OneDrive\Desktop\NLP Programs>python 8_POS_Tags.py
POS Tags: [('The', 'DT'), ('dog', 'NN'), ('sat', 'VBD'), ('on', 'IN'), ('the', 'DT'), ('rug', 'NN')]
