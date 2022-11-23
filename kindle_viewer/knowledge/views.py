from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.core.files import File
from django.core.files.storage import FileSystemStorage
'''models '''
from .models import Book, Document, HighLight
'''another modules'''
from .processing_data import processing_data
'''forms'''
from .forms import NoteForm

# Create your views here.

'''homepage'''
def index(request):
    return render(request, 'knowledge/index.html')

'''this is a page where user can upload individual kindle file'''
def upload(request):
    context = {}
    if request.method == 'POST':
        file = request.FILES['file']
        fs = FileSystemStorage()
        name = fs.save(file.name, file)
        context['url'] = fs.url(name)
        document = Document.objects.create(name=file.name, file=file)
    return render(request, 'knowledge/upload.html', context)

'''Functionality below uses last uploaded kindle document, stored by user in database to create 
various items in tables:
    -- book (it works as primary key for highlight table model)
    -- highlights 
    -- notes '''
def process(request):
    context = {}
    #creating object which is a dictionary where the keys are book titles, and the items are distinct notes
    wanted_object = Document.objects.all().last()
    content_list = processing_data(wanted_object)

    for key in content_list[0]:
        if not Book.objects.filter(title=str(key)).exists():
            book = Book.objects.create(title=str(key))
            book.save()

    for key in content_list[0]:
        book = Book.objects.get(title=str(key))
        for item in content_list[1][key]:
            if not HighLight.objects.filter(note=str(item[0])).exists():
                note = HighLight.objects.create(book=book, note=str(item[0]), date_added=item[1])


    context['lines'] = content_list[0]

    return render(request, 'knowledge/index.html')

def create_note(request):

    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.cleaned_data['note']
            print(note)

        return render(request, 'knowledge/upload.html')

    else:
        form = NoteForm()

    return render(request, 'knowledge/create.html', {'form': form})