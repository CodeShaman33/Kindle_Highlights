from django import forms



class NoteForm(forms.Form):

    note = forms.CharField(label='place your thoughts', max_length=1000)