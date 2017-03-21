from django import forms


class FaceForm(forms.Form):
    main_field = forms.CharField(label='common_interface_field', max_length=50)
