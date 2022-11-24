from django.contrib import admin
from django.urls import path
from . import views

app_name = 'knowledge'


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('process/', views.process, name='process'),
    path('create/', views.create_note, name='create'),
    path('books/', views.books, name='books'),
    path('book/(<int:book_id>)/', views.book, name='book')

]