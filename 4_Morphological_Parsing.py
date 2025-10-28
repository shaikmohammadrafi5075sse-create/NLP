def pluralize(noun):
    # State 0: Start
    # State 1: Ends with 's', 'sh', 'ch', 'x', or 'z' → add 'es'
    # State 2: Ends with a consonant + 'y' → replace 'y' with 'ies'
    # State 3: Else → add 's'
    
    if noun.endswith(('s', 'sh', 'ch', 'x', 'z')):
        return noun + 'es'
    elif noun.endswith('y') and noun[-2].lower() not in 'aeiou':
        return noun[:-1] + 'ies'
    else:
        return noun + 's'

# Test cases
nouns = ["cat", "dog", "bus", "box", "baby", "church", "fox", "boy", "quiz"]
for word in nouns:
    plural = pluralize(word)
    print(f"{word} -> {plural}")

#----------------------OUTPUT--------------------------------------

C:\Users\HP\OneDrive\Desktop\NLP Programs>python 4_Morphological_Parsing.py
cat -> cats
dog -> dogs
bus -> buses
box -> boxes
baby -> babies
church -> churches
fox -> foxes
boy -> boys
quiz -> quizes