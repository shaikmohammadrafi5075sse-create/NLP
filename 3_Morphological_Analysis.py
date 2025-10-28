import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required resources (run once)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

text = "The children are playing games in the gardens."

# Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Part-of-speech tagging
pos_tags = nltk.pos_tag(tokens)
print("POS Tags:", pos_tags)

# Stemming
stemmer = PorterStemmer()
stems = [stemmer.stem(token) for token in tokens]
print("Stems:", stems)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(token) for token in tokens]
print("Lemmas:", lemmas)

#-----------------OutPut-------------------------------

Tokens: ['The', 'children', 'are', 'playing', 'games', 'in', 'the', 'gardens', '.']
POS Tags: [('The', 'DT'), ('children', 'NNS'), ('are', 'VBP'), ('playing', 'VBG'), ('games', 'NNS'), ('in', 'IN'), ('the', 'DT'), ('gardens', 'NNS'), ('.', '.')]
Stems: ['the', 'children', 'are', 'play', 'game', 'in', 'the', 'garden', '.']
Lemmas: ['The', 'child', 'are', 'playing', 'game', 'in', 'the', 'garden', '.']