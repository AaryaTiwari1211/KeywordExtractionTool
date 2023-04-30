from django.shortcuts import render, redirect
from django.contrib import messages
import PyPDF2
from .models import Text, Url, Document
from .graph_generator import graph_generator
# from .keyword_extractor import extract_keywords
from .final_tool import extract_keywords
from .wordcloud_generator import wordcloud_generator
from .doctext_generator import doc_extractor
from .urlextractor import url_keywords
import matplotlib.pyplot as plt
plt.switch_backend('agg')


def index(request):
    return render(request, 'main/home.html')


def tool(request):
    keywords = []
    frequency = []
    context = {}
    doc = request.FILES
    if request.method == 'POST' and request.POST['text_title'] != '' and request.POST['text_data'] != '':
        text_title = request.POST['text_title']
        text_data = request.POST['text_data']
        wordcloud_generator(text_data)
        keywords, frequency, dict = extract_keywords(text_data)
        graph_generator(keywords, frequency)
        new_text = Text(text_title=text_title, text_data=text_data)
        new_text.save()

        context = {
            'keywords': keywords,
        }
        messages.success(
            request, f'Your text has been processed and keywords are in the right ->!')
    elif request.method == 'POST' and request.POST['url_title'] != '' and request.POST['url'] != '':
        url_title = request.POST['url_title']
        url = request.POST['url']
        url_text = url_keywords(url)
        keywords, frequency, dict = extract_keywords(url_text)
        wordcloud_generator(url_text)
        graph_generator(keywords, frequency)
        new_url = Url(url_title=url_title, url=url)
        new_url.save()

        context = {
            'keywords': keywords,
        }
        messages.success(
            request, f'Your text has been processed and keywords are in the right ->!')
    elif request.method == 'POST' and request.POST['text_title'] == '' and request.POST['text_data'] == '' and request.POST['url_title'] == '' and request.POST['url'] == '':
        txtfile = request.FILES['txtfile']
        if txtfile.name.endswith(".txt"):
            file_text = txtfile.read().decode('utf-8')
        else:
            messages.success(request, f'Invalid File Type!!')
        keywords, frequency, dict = extract_keywords(file_text)
        wordcloud_generator(file_text)
        graph_generator(keywords, frequency)
        new_file = Document(doc=txtfile)
        new_file.save()
        context = {
            'keywords': keywords,
        }
        messages.success(
            request, f'Your text has been processed and keywords are in the right ->!')
    return render(request, 'main/tool.html', context)


def nlp(request):
    return render(request, 'main/nlp.html')


def about(request):
    return render(request, 'main/about.html')
