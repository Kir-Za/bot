from django import forms
from django.forms import ModelForm
from .models import MyNote


class SearchForm(forms.Form):
    search_field = forms.CharField(label='common_interface_field', max_length=50)


class AddNoteForm(ModelForm):
    class Meta:
        model = MyNote
        fields = ['title', 'keys', 'text_body']
