from nltk.stem import PorterStemmer

# List of words to stem
words = ['caresses', 'flies', 'dies', 'mules', 'denied', 'agreed', 'owned', 'humbled', 'sized', 'meeting', 'stating', 'siezing', 'itemization', 'sensational', 'traditional', 'reference', 'colonizer', 'plotted']

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

# Perform stemming on each word
stems = [stemmer.stem(word) for word in words]

# Print the original words and their stems
for original, stemmed in zip(words, stems):
    print(f"{original} → {stemmed}")

#------------OUTPUT------------------------------------

C:\Users\HP\OneDrive\Desktop\NLP Programs>python 5_Porter_Stemmer.py
caresses → caress
flies → fli
dies → die
mules → mule
denied → deni
agreed → agre
owned → own
humbled → humbl
sized → size
meeting → meet
stating → state
siezing → siez
itemization → item
sensational → sensat
traditional → tradit
reference → refer
colonizer → colon
plotted → plot