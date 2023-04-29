import re
import string
from collections import Counter
import spacy
import nltk
from nltk import FreqDist
from nltk import word_tokenize
import numpy as np
import pandas as pd
import networkx as nx
from nltk.sentiment import SentimentIntensityAnalyzer

from PIL import Image




def build_vocabulary(page: list) -> list:
    # Builds vocabulary with all the words
    # present in the list page.
    vocab = list(set(page))
    vocab.sort()

    vocab_dict = {}
    for index, word in enumerate(vocab):
        vocab_dict[word] = index
    return vocab_dict


def build_context(page: str, co_ocurrence_vectors: pd.DataFrame) -> pd.DataFrame:
    for index, element in enumerate(page):
        start = 0 if index-2 < 0 else index-2
        finish = len(page) if index+2 > len(page) else index+3
        context = page[start:index]+page[index+1:finish]
        for word in context:
            co_ocurrence_vectors.loc[element, word] = (
                co_ocurrence_vectors.loc[element, word]+1)
    return co_ocurrence_vectors


def extract_keywords(text):
    print(text)
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    len(text)
    len(doc)
    for ent in doc.ents:
        print(ent.text, ent.label_)
    stopwords = [w for w in doc if w.is_stop == True]

    text2 = [w for w in doc if w.is_stop == False and w.pos_ != "PUNCT"]

    delimiters = [w for w in doc if w.pos_ == "PUNCT"]
    delimiter = str(delimiters)

    text3 = " ".join([token.lemma_ for token in text2])
    print(text3)

    keyword = str(text3).split()

    frequency = FreqDist(keyword)
    print(frequency.most_common())

    stopword = str(stopwords)
    st = stopword.split()

    keylist = []
    keyword = list(frequency.keys())
    keyword2 = str(frequency.keys())
    keylist = keyword
    print(keyword2)
    vocab_dict = build_vocabulary(text2)
    print(vocab_dict)
    vocab_dict2 = build_vocabulary(frequency.keys())
    print(vocab_dict2)
    co_ocurrence_vectors2 = pd.DataFrame(
        np.zeros([len(vocab_dict2), len(vocab_dict2)]),
        index=vocab_dict2.keys(),
        columns=vocab_dict2.keys()
    )
    print(co_ocurrence_vectors2)

    co_ocurrence_vectors2 = build_context(keyword, co_ocurrence_vectors2)

    print(co_ocurrence_vectors2)
    print(frequency.most_common())
    print("\n")
    print(frequency.values())
    print("\n")
    frequency_str = str(frequency.values())
    print(frequency_str)
    print("\n")
    for i in range(len(frequency_str)):
        frequency_str[i]
        print(frequency_str[16])
    g = nx.Graph()

    nodes = nlp(str(keylist))
    nodes

    g.add_node(nodes)

    nltk.download('vader_lexicon')

    nltk.download('punkt')

    sia = SentimentIntensityAnalyzer()

    tokens = nltk.word_tokenize(text)

    scores = {}
    for token in tokens:
        if token in keylist:
            scores[token] = sia.polarity_scores(token)["compound"]
    print(scores)
    ratios = {}
    degree = g.degree(nodes)
    freq = list(dict(g.degree()).values()).count(degree)
    ratio = degree / freq
    ratios[nodes] = ratio
    print(ratios)
    degree = {word: frequency[word] for word in set(tokens)}

    # Calculate the degree-to-frequency ratio for each token
    ratios = {}
    for word in degree:
        if frequency[word] == 0:
            ratios[word] = 0
        else:
            ratios[word] = degree[word] / frequency.freq(word)

    # Print the ratios
    print('ratios are: ')
    print(ratios)
 
    sorted_dict = {k: v 
                    for k, v in sorted(
                        ratios.items(), key=lambda item: item[1], reverse=True)
                }
    print('sorted: ')
    print(sorted_dict)
    values_array = list(sorted_dict.values())
    new_list = [i for i in values_array if i != 0]
    print(new_list)
    sorted_dict = my_dict = {k: v for k, v in sorted_dict.items() if v != 0}
    keywords_to_extract = len(sorted_dict) 
    
    print('keywords to extract: ')
    print(keywords_to_extract)
    # print(sorted_dict)

    sort = list(sorted_dict)
    final = sort[:keywords_to_extract]
    print('final: ')
    print(final)
    final_string = " ".join(str(item) for item in final)
    print(final_string)
    print(len(final))
    print(len(new_list))
    return final , new_list , sorted_dict
