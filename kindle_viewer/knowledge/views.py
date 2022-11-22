from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.core.files import File
from django.core.files.storage import FileSystemStorage
'''models '''
from .models import Book, Document, HighLight

# Create your views here.


def index(request):
    return render(request, 'kindle/index.html')