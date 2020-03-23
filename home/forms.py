from django import forms
from .models import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['text']
        labels = {'text': 'Enter a location'}
        widgets = {'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter something like quan 7, quan 1, go vap, thu duc, ...', 'size': 60})}
