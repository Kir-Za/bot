from django import forms


class SearchForm(forms.Form):
    search_field = forms.CharField(label='common_interface_field', max_length=50)
