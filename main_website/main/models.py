from django.db import models


class Text(models.Model):
    text_title = models.CharField(max_length=20)
    text_data = models.TextField(max_length=1000000)
    # wordcloud = models.ImageField(upload_to="media/images")
    
    def __str__(self):
        return self.text_title

class Url(models.Model):
    url_title = models.CharField(max_length=20)
    url = models.URLField(max_length=200)
    def __str__(self):
        return self.url_title

class Document(models.Model):
    doc = models.FileField(upload_to='files/')
    def __str__(self):
        return self.doc
