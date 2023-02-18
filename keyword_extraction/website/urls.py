from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('tool/',views.tool,name='tool'),
    path('nlp/',views.nlp,name='nlp'),
] 