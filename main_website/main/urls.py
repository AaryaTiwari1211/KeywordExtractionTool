from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('tool/',views.tool,name='tool'),
    path('about/',views.about,name='about'),
    path('nlp/',views.nlp,name='nlp'),
    path('graphs/',views.graph,name='graph'),
    path('algorithm/',views.algorithm,name='algorithm'),
]
