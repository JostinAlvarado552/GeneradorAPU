from django import forms

class IDForm(forms.Form):
    id = forms.CharField(label='ID', max_length=100)
