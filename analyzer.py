ximport nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

from nltk import WordNetLemmatizer

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def create_cloud(source="./master.txt", img_name="WordCloud.png"):
    # Reading and tokenization
    text = open(source, "r", encoding = "UTF-8")

    raw = text.read()
    tokens = word_tokenize(raw)

    # Normalization
    tokens = [word for word in tokens if word.isalpha()]
    tokens = [word.lower() for word in tokens]

    # Removing stop words
    tokens = [word for word in tokens if not word in stopwords.words("english")]

    # Lemmatization

    lemma = WordNetLemmatizer()

    tokens = [lemma.lemmatize(token, pos = "a") for token in tokens] #For Adjectives
    tokens = [lemma.lemmatize(token, pos = "s") for token in tokens] #For Sattelite Adjectives
    tokens = [lemma.lemmatize(token, pos = "r") for token in tokens] #For Adverbs
    tokens = [lemma.lemmatize(token, pos = "n") for token in tokens] #For Nouns
    tokens = [lemma.lemmatize(token, pos = "v") for token in tokens] #For Verbs

    word_count = Counter(tokens)
    print(word_count.most_common(10))

    # Creating the Word Cloud
    word_string = ""
    for token in tokens:
        word_string += token + " "

    wc = WordCloud(width=400, height=400, collocations = False, background_color = 'black', max_words=100)
    cloud = wc.generate(word_string)

    plt.figure(figsize=(200, 200))
    plt.clf()
    plt.imshow(cloud)
    plt.axis('off')
    plt.title(img_name.split('.')[0:-1] + " Cloud")
    plt.savefig(img_name)
    plt.show()
    
    return word_count

create_cloud(img_name="Love The Way You Lie.png")
