def top_down_parser(tokens, grammar, start_symbol):
    stack = [start_symbol]
    print(f"Initial Stack: {stack}")
    tokens = tokens[:]  # Make a copy to avoid modifying original
    while stack:
        top = stack.pop()
        if top in grammar:
            production = grammar[top][0]
            print(f"Expanding {top} -> {production}")
            stack.extend(reversed(production))
        elif tokens and top == tokens[0]:
            print(f"Matching terminal: {top}")
            tokens.pop(0)
        else:
            print("Parsing failed.")
            return False
    return not tokens

grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': [['the']],
    'N': [['cat']],
    'V': [['sees']]
}
tokens = ['the', 'cat', 'sees', 'the', 'cat']
result = top_down_parser(tokens, grammar, 'S')
print("Parsing Successful!" if result else "Parsing Failed!")

------------------------------------OUTPUT-------------------------------

C:\Users\HP\OneDrive\Desktop\NLP Programs>python Act_Tokens.py
Initial Stack: ['S']
Expanding S -> ['NP', 'VP']
Expanding NP -> ['Det', 'N']
Expanding Det -> ['the']
Matching terminal: the
Expanding N -> ['cat']
Matching terminal: cat
Expanding VP -> ['V', 'NP']
Expanding V -> ['sees']
Matching terminal: sees
Expanding NP -> ['Det', 'N']
Expanding Det -> ['the']
Matching terminal: the
Expanding N -> ['cat']
Matching terminal: cat
Parsing Successful!