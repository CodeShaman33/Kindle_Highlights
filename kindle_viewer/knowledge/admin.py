from django.contrib import admin
from .models import Book, HighLight, Document

# Register your models here.
admin.site.register(Book)
admin.site.register(Document)
admin.site.register(HighLight)

