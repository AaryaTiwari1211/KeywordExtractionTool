
from wordcloud import WordCloud, STOPWORDS
from .final_tool import extract_keywords
import matplotlib.pyplot as plt
stopw = set(STOPWORDS)
def wordcloud_generator(text):
    keywords , frequency , dict = extract_keywords(text)
    convert_text = " ".join(str(item) for item in keywords)
    word_cloud = WordCloud(stopwords=stopw, background_color="white", max_words=100,
    contour_width=3, contour_color='steelblue', width=800, height=400, max_font_size=100, min_font_size=10, random_state=42
    ).generate(convert_text)
    word_cloud = WordCloud(
        stopwords=stopw,
        background_color="white",
        max_words=100,
        contour_width=3,
        contour_color='steelblue',
        width=800,
        height=400,
        max_font_size=100,
        min_font_size=10, random_state=42
    ).generate_from_frequencies(dict)
    plt.figure(figsize=[20, 10])
    plt.imshow(
        word_cloud, 
        interpolation='bilinear'
    )
    plt.axis("off")
    plt.savefig("media/images/wordcloud.png")

