from django.urls import path

from . import views

app_name = 'knowledge'

urlpatterns = [
    path( '', views.index, name = 'index' ),
    path( 'upload/', views.upload, name = 'upload' ),
    path( 'process/', views.process, name = 'process' ),
    path( 'books/', views.books, name = 'books' ),
    path( 'book/(<int:book_id>)/', views.book, name = 'book' ),
    path( 'create/(<int:entry_id>)/', views.create, name = 'create' ),
    path( 'notes/(<int:entry_id>)/', views.notes, name = 'notes' ),
    path( 'test/', views.test, name = 'test' ),
    path( 'book_delete/(<int:book_id>)/', views.book_delete, name = 'book_delete' ),

    path( '/sample-index', views.sampleIndex, name = 'sample-index' ),
    path( '/sample-book', views.sampleBook, name = 'sample-book' ),
    path( '/sample-books', views.sampleBooks, name = 'sample-books' ),

]
