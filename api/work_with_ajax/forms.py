from django import forms
from .models import ForTestOnly


class ForForm(forms.ModelForm):

    class Meta:

        model = ForTestOnly
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name here'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'author': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'description': 'My Description',
        }
