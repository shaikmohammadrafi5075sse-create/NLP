import re

# Initial naive POS tagger (assigns all to 'NN' except known verbs)
def initial_pos_tag(tokens):
    pos_tags = []
    verb_list = {'is', 'are', 'run', 'running', 'agreed', 'sat'}  # sample verbs
    for token in tokens:
        if token.lower() in verb_list:
            pos_tags.append((token, 'VBD'))  # naive: assign all verbs as past tense
        else:
            pos_tags.append((token, 'NN'))   # default noun
    return pos_tags

# Transformation rule: if tag is VBD and word ends with 'ing', change tag to VBG
def apply_transformation_rules(pos_tags):
    transformed_tags = []
    for word, tag in pos_tags:
        if tag == 'VBD' and word.endswith('ing'):
            # Apply transformation rule
            transformed_tags.append((word, 'VBG'))
        else:
            transformed_tags.append((word, tag))
    return transformed_tags

# Example sentence
sentence = "Mary is running and Fred agreed"
tokens = re.findall(r"\w+", sentence)

# Step 1: Initial tagging
initial_tags = initial_pos_tag(tokens)
print("Initial Tags:", initial_tags)

# Step 2: Apply transformation rules
final_tags = apply_transformation_rules(initial_tags)
print("Transformed Tags:", final_tags)

#------------------------------OUTPUT------------------------------

C:\Users\HP\OneDrive\Desktop\NLP Programs>python 10_Tagging.py
Initial Tags: [('Mary', 'NN'), ('is', 'VBD'), ('running', 'VBD'), ('and', 'NN'), ('Fred', 'NN'), ('agreed', 'VBD')]
Transformed Tags: [('Mary', 'NN'), ('is', 'VBD'), ('running', 'VBG'), ('and', 'NN'), ('Fred', 'NN'), ('agreed', 'VBD')]
