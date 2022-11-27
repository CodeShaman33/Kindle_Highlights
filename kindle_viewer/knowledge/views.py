from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.core.files import File
from django.core.files.storage import FileSystemStorage
'''models '''
from .models import Book, Document, HighLight
'''another modules'''
from .processing_data import processing_data
'''forms'''
from .forms import NoteForm
'''decorators'''
from django.contrib.auth.decorators import login_required

# Create your views here.

'''homepage'''
def index(request):
    return render(request, 'knowledge/index.html')

'''this is a page where user can upload individual kindle file'''
@login_required
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
@login_required
def process(request):
    context = {}
    #creating object which is a dictionary where the keys are book titles, and the items are distinct notes
    wanted_object = Document.objects.all().last()
    content_list = processing_data(wanted_object)

    for key in content_list[0]:
        if not Book.objects.filter(title=str(key)).exists():
            book = Book.objects.create(title=str(key))
            book.save()

    '''every key in function below is individual book title, and for that key the function assigns new highlights, 
    but first it checks if the highlight already exist in database'''
    for key in content_list[0]:
        book = Book.objects.get(title=str(key))
        for item in content_list[1][key]:
            if not HighLight.objects.filter(note=str(item[0])).exists():
                note = HighLight.objects.create(book=book, note=str(item[0]), date_added=item[1])


    context['lines'] = content_list[0]

    return render(request, 'knowledge/index.html')

'''This function displays all books in database as interactive elements'''
@login_required
def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'knowledge/books.html', context)

'''this function create a page with all highlight associated with book user choosed'''
@login_required
def book(request, book_id):
    book = Book.objects.get(id=book_id)
    entries = HighLight.objects.filter(book=book)
    context = {'book_name': book.title, 'entries': entries}
    return render(request, 'knowledge//book.html', context)



'''this function create a blank form which user can fill with his thoughts about specyfic highlight
It uses existing instance of a model'''
@login_required
def create(request, entry_id):
    highlight = HighLight.objects.get(id=entry_id)

    if request.method == 'POST':
        form = NoteForm(data=request.POST, instance=highlight)

        if form.is_valid():
            form.save()
            return redirect('knowledge:books')

    else:
        form = NoteForm(instance=highlight)

    return render(request, 'knowledge/create.html', {'form': form})

'''This function diplays thoughts associated with specyfic highlight.'''
@login_required
def notes(request, entry_id):
    highlight = HighLight.objects.get(id=entry_id)
    note = highlight.note
    thought = highlight.thought
    print(note, thought)
    context = {'note': note, 'thought': thought}
    return render(request, 'knowledge//notes.html', {'note': note, 'thought': thought})

'''test function to  render test page'''
def test(request):

    return render(request, 'knowledge/base.html')

