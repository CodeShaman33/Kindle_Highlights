from django import forms
from .models import HighLight


class NoteForm(forms.ModelForm):

    class Meta:
        model = HighLight
        fields = ['thought']
        labels = {'note': 'place your thought'}