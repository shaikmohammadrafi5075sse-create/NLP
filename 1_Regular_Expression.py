import re

# Example text
text = "The rain in Spain falls mainly in the plain."

# Search for the word 'Spain'
result_search = re.search(r'Spain', text)
if result_search:
    print("Found 'Spain' at position:", result_search.start())
else:
    print("'Spain' not found.")

# Match beginning of the string
result_match = re.match(r'The', text)
if result_match:
    print("Text starts with 'The'.")
else:
    print("Text does not start with 'The'.")

# Find all words ending with 'ain'
result_findall = re.findall(r'\b\w*ain\b', text)
print("Words ending with 'ain':", result_findall)

# Replace all occurrences of 'ain' with '___'
result_sub = re.sub(r'ain', '___', text)
print("Text after replacement:", result_sub)

#-------------------output----------------

C:\Users\HP\OneDrive\Desktop\NLP Programs>python 1_Regular_Expression.py
Found 'Spain' at position: 12
Text starts with 'The'.
Words ending with 'ain': ['rain', 'Spain', 'plain']
Text after replacement: The r___ in Sp___ falls m___ly in the pl___.