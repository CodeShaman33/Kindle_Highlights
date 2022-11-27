from django import forms
from .models import HighLight

'''this is a form used to updating existing Highlight model'''
class NoteForm(forms.ModelForm):

    class Meta:
        model = HighLight
        fields = ['thought']
        labels = {'note': 'place your thought'}