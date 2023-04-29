from wordcloud import WordCloud, STOPWORDS
# from .keyword_extractor import extract_keywords
import matplotlib.pyplot as plt
stopw = set(STOPWORDS)


def wordcloud_generator(text):
    # text , freq , dict= extract_keywords(text)
    # convert_text = " ".join(str(item) for item in text)
    # word_cloud = WordCloud(stopwords=stopw, background_color="white", max_words=100,
    # contour_width=3, contour_color='steelblue', width=800, height=400, max_font_size=100, min_font_size=10, random_state=42
    # ).generate(convert_text)
    # word_cloud = WordCloud(
    #     stopwords=stopw,
    #     background_color="white",
    #     max_words=100,
    #     contour_width=3,
    #     contour_color='steelblue',
    #     width=800,
    #     height=400,
    #     max_font_size=100,
    #     min_font_size=10, random_state=42
    # ).generate_from_frequencies({"Sad":8,"Happy":5,"Gloomy":4})
    # word_cloud.to_file("media/images/wordcloud.png")
    wc = WordCloud.generate_from_frequencies({"Gloomy": 6, "Hello": 2})
    plt.figure(figsize=[20, 10])
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()
