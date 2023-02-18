from django.db import models

class Document(models.Model):
    text = models.TextField(max_length=1000000)