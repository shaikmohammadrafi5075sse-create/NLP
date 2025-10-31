import spacy

nlp = spacy.load("en_core_web_sm")
sentence = "The cat chases the mouse"
doc = nlp(sentence)

for token in doc:
    print(f"{token.text:<10} {token.dep_:<10} {token.head.text:<10}")

-----------------------------------OUTPUT--------------------------------------

C:\Users\HP\OneDrive\Desktop\NLP Programs>python dependancy_parsing.py
The        det        cat
cat        nsubj      chases
chases     ROOT       chases
the        det        mouse
mouse      dobj       chases