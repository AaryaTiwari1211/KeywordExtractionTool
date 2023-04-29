import re
from collections import Counter
import spacy

def get_stopwords(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    stopwords = [w.text.lower() for w in doc if w.is_stop == True]
    return stopwords


def get_phrase_list(text, stopwords):
    """Returns a list of candidate phrases."""
    # Remove special characters and digits
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = re.sub('\s+', ' ', text)

    # Tokenize the text into words
    words = text.split()

    # Remove stop words
    words = [word.lower() for word in words if word.lower() not in stopwords]

    # Combine adjacent words into phrases
    phrases = []
    for i in range(len(words)-1):
        phrase = words[i] + ' ' + words[i+1]
        phrases.append(phrase)

    return phrases


def get_word_scores(phrases):
    """Returns a dictionary of word scores."""
    word_freq = Counter()
    word_degree = Counter()
    for phrase in phrases:
        words = phrase.split()
        word_freq.update(words)
        word_degree.update(set(words))
    word_scores = {}
    for word in word_freq:
        word_scores[word] = word_degree[word] / word_freq[word]
    return word_scores


def get_phrase_scores(phrases, word_scores):
    """Returns a dictionary of phrase scores."""
    phrase_scores = {}
    for phrase in phrases:
        words = phrase.split()
        phrase_score = sum([word_scores[word] for word in words])
        phrase_scores[phrase] = phrase_score
    return phrase_scores


def get_top_phrases(text, num_phrases=10):
    """Returns the top n phrases with highest scores."""
    stopwords = get_stopwords(text)
    phrases = get_phrase_list(text, stopwords)
    word_scores = get_word_scores(phrases)
    phrase_scores = get_phrase_scores(phrases, word_scores)
    top_phrases = sorted(phrase_scores.items(),
                         key=lambda x: x[1], reverse=True)
    return top_phrases[:num_phrases]


text = """The World Health Organization (WHO) is a specialized agency of the United Nations responsible for international public health. The WHO Constitution, which establishes the agency's governing structure and principles, states its main objective as "the attainment by all peoples of the highest possible level of health."""
top_phrases = get_top_phrases(text)
for phrase, score in top_phrases:
    print(phrase, score)
