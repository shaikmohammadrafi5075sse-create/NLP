import re

# Define regex-based POS tagging rules as (pattern, tag) tuples
rules = [
    (r'.*ing$', 'VBG'),      # gerunds
    (r'.*ed$', 'VBD'),       # past tense verbs
    (r'.*es$', 'VBZ'),       # third person singular verbs
    (r'.*ly$', 'RB'),        # adverbs
    (r'.*ion$', 'NN'),       # nouns ending with 'ion'
    (r'.*ment$', 'NN'),      # nouns ending with 'ment'
    (r'.*ful$', 'JJ'),       # adjectives ending with 'ful'
    (r'.*ous$', 'JJ'),       # adjectives ending with 'ous'
    (r'.*able$', 'JJ'),      # adjectives ending with 'able'
    (r'.*ness$', 'NN'),      # nouns ending with 'ness'
    (r'^[A-Z][a-z]+$', 'NNP'), # proper nouns
    (r'.*', 'NN')            # default: noun
]

def regex_pos_tag(tokens):
    tags = []
    for token in tokens:
        for pattern, tag in rules:
            if re.fullmatch(pattern, token):
                tags.append((token, tag))
                break
    return tags

# Example sentence
sentence = "Mary happily agreed to help running dogs quickly."
tokens = re.findall(r"\w+", sentence)
tags = regex_pos_tag(tokens)
print("POS Tags:", tags)

#-------------------OUTPUT---------------------------

C:\Users\HP\OneDrive\Desktop\NLP Programs>python 9th.py
POS Tags: [('Mary', 'NNP'), ('happily', 'RB'), ('agreed', 'VBD'), ('to', 'NN'), ('help', 'NN'), ('running', 'VBG'), ('dogs', 'NN'), ('quickly', 'RB')]
