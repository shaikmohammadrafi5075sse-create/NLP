import nltk
from nltk import CFG
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog'
V -> 'sees' | 'likes'
""")
parser = nltk.ChartParser(grammar)
sentence = ['the', 'cat', 'sees', 'a', 'dog']
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()

    -----------------OUTPUT----------------------------

    C:\Users\HP\OneDrive\Desktop\NLP Programs>python Act1CFG.py
(S (NP (Det the) (N cat)) (VP (V sees) (NP (Det a) (N dog))))
             S
      _______|____
     |            VP
     |        ____|___
     NP      |        NP
  ___|___    |     ___|___
Det      N   V   Det      N
 |       |   |    |       |
the     cat sees  a      dog
