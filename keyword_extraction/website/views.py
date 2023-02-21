from django.shortcuts import render
from .models import Document

# Create your views here.


def index(request):
    return render(request, 'website/home.html')


def tool(request):
    return render(request, 'website/tool.html')


def nlp(request):
    return render(request, 'website/nlp.html')

def about(request):
    return render(request, 'website/about.html')

def keyword_extracter(request):
    if request.method == 'POST':
        text = request.POST['text-input']
        url = request.POST['text-input']
        file = request.POST['text-input']
        
