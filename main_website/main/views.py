from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Text
from .keyword_extractor import extract_keywords, wordcloud_generator
from PIL import Image
import base64
from io import BytesIO

def index(request):
    return render(request, 'main/home.html')


def tool(request):
    keywords = []
    context = {}
    if request.method == 'POST':
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
    return render(request, 'main/tool.html', context)

def nlp(request):
    return render(request, 'main/nlp.html')

def about(request):
    return render(request, 'main/about.html')
