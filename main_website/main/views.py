from django.shortcuts import render , redirect
from django.contrib import messages
from .models import Text
from .keyword_extractor import extract_keywords

def index(request):
    return render(request, 'main/home.html')

def tool(request):
    keywords = []
    if request.method == 'POST':
        text_title = request.POST['text_title']
        text_data = request.POST['text_data']
        new_text = Text(text_title=text_title,text_data=text_data)
        new_text.save()
        keywords = extract_keywords(text_data)
        messages.success(request, f'Your text has been added to the database!')
    return render(request, 'main/tool.html',{'keywords': keywords})


def nlp(request):
    return render(request, 'main/nlp.html')

def about(request):
    return render(request, 'main/about.html')
