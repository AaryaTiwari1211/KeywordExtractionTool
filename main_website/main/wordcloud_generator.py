from wordcloud import WordCloud, STOPWORDS
from .keyword_extractor import extract_keywords

stopw = set(STOPWORDS)

def wordcloud_generator(text):
    text = extract_keywords(text)
    convert_text = " ".join(str(item) for item in text)
    word_cloud = WordCloud(stopwords=stopw, background_color="white", max_words=100,
    contour_width=3, contour_color='steelblue', width=800, height=400, max_font_size=100, min_font_size=10, random_state=42
    ).generate(convert_text)
    img = word_cloud.to_file("media/images/wordcloud.png")
    return img
