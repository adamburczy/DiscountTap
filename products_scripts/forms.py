from django import forms

class SearchForm(forms.Form):
    item = forms.CharField(label='czego szukasz?', max_length=100)