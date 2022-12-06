from django.db import models
'''authorization '''
from django.contrib.auth.models import User

# Create your models here.

'''In this module are models that stores:
    -- book titles
    -- Highlights
    -- Notes made by user, associated with individual highlights
    -- It is still test version of the app so there are no arguments inside model fields yet'''

'''This model is made to store .txt documents extracted from kindle device and uploaded onto database'''
class Document(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField()
    owner = models.ForeignKey(User,  on_delete=models.CASCADE)

'''This model stores Books as titles which will be primary keys for highlights in model below '''
class Book(models.Model):
    title = models.CharField(max_length=600, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

'''This model stores every highlights the file_handling module will give'''
class HighLight(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    note = models.TextField()
    date_added = models.TextField()
    thought = models.TextField(blank=True)

    def __str__(self):
        return self.note

