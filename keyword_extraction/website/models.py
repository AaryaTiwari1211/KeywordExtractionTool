from django.db import models


class Document(models.Model):
    text_id = models.AutoField(primary_key=True)
    url = models.URLField(null=True)
    docs = models.FileField(null=True)
    doc_name = models.TextField(max_length=50)
    text = models.TextField(max_length=1000000)

    def __str__(self):
        return self.doc_name
