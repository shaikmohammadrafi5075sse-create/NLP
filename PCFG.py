from nltk import PCFG
from nltk.parse import ViterbiParser

pcfg_grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.9] | 'John' [0.1]
VP -> V NP [0.5] | V [0.5]
Det -> 'the' [1.0]
N -> 'dog' [0.5] | 'cat' [0.5]
V -> 'sees' [1.0]
""")

parser = ViterbiParser(pcfg_grammar)
sentence = ['John', 'sees', 'the', 'dog']

for tree in parser.parse(sentence):
    print(tree)
    print(f"Probability: {tree.prob()}")

-----------------------OUTPUT---------------------------------------------------

(S (NP John) (VP (V sees) (NP (Det the) (N dog)))) (p=0.0225)
Probability: 0.022500000000000003