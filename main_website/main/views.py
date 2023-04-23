from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Text, Url, Document
from .keyword_extractor import extract_keywords
from .wordcloud_generator import wordcloud_generator
from .doctext_generator import doc_extractor
from .urlextractor import url_keywords
from PIL import Image
import base64
from io import BytesIO


def index(request):
    return render(request, 'main/home.html')


def tool(request):
    keywords = []
    context = {}
    doc = request.FILES
    if request.method == 'POST' and request.POST['text_title'] != '' and request.POST['text_data'] != '':
        text_title = request.POST['text_title']
        text_data = request.POST['text_data']
        img = wordcloud_generator(text_data)
        keywords = extract_keywords(text_data)
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
        img = wordcloud_generator(url_text)
        keywords = extract_keywords(url_text)
        new_url = Url(url_title=url_title, url=url)
        new_url.save()
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
