from django.contrib import admin
from .models import Text , Url , Document

admin.site.register(Text)
admin.site.register(Url)
admin.site.register(Document)