import re
import string
from collections import Counter

def extract_keywords(text):
    # Split text into sentences
    sentences = re.split('\.|!|\?', text)
    
    # Remove punctuation and convert to lowercase for each sentence
    sentence_words = []
    for sentence in sentences:
        sentence = re.sub('[%s]' % re.escape(string.punctuation), '', sentence.lower())
        sentence_words.append(re.split('\W+', sentence))
    
    # Flatten list of sentence words into a single list
    words = [word for sentence in sentence_words for word in sentence]
    
    # Create a dictionary of word frequency
    word_freq = Counter(words)
    
    # Set of stop words
    stop_words = set(['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than'])
    
    # Calculate word scores
    word_scores = {}
    for word in word_freq:
        if len(word) > 1:
            word_degree = sum(word in sentence for sentence in sentence_words)
            word_frequency = word_freq[word]
            word_score = word_frequency / word_degree
            word_scores[word] = word_score
    
    # Calculate phrase scores
    phrase_scores = {}
    for sentence in sentence_words:
        for i in range(len(sentence)):
            if sentence[i] not in stop_words and len(sentence[i]) > 1:
                phrase_words = sentence[max(0, i-2):i+3]
                phrase_words = [word for word in phrase_words if word not in stop_words and len(word) > 1]
                if phrase_words:
                    phrase = " ".join(phrase_words)
                    if all(word in word_scores for word in phrase_words):
                        phrase_scores[phrase] = sum(word_scores[word] for word in phrase_words)
    
    # Sort phrases by score
    sorted_phrases = sorted(phrase_scores.items(), key=lambda x: x[1], reverse=True)
    
    # Return top 10 phrases
    return [x[0] for x in sorted_phrases[:-1]]

text = """The story follows Arima Kousei, a skilled pianist. However, he hasn't played since he played for his mother who died a few years ago. One day Arima meets a brilliant violinist at the park. After their meeting she tries to guide Arima back into the world of music."""

keywords = extract_keywords(text)
print(keywords)
