from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'website/home.html')
def tool(request):
    return render(request,'website/tool.html')
def nlp(request):
    return render(request,'website/nlp.html')