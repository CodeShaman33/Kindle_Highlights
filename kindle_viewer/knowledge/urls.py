from django.contrib import admin
from django.urls import path
from . import views

app_name = 'knowledge'


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('process/', views.process, name='process'),
    path('books/', views.books, name='books'),
    path('book/(<int:book_id>)/', views.book, name='book'),
    path('create/(<int:entry_id>)/', views.create, name='create'),
    path('notes/', views.notes, name='notes')

]