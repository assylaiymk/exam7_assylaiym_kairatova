from django import forms
from django.forms import widgets


class BookForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='Name')
    email = forms.EmailField(max_length=200, required=True, label='Email')
    # author = forms.CharField(max_length=10, required=True, label='Author')
    text = forms.CharField(max_length=2000,
                           required=True,
                           label='Text',
                           widget=widgets.Textarea)
