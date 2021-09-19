from django import forms
from .models import University


class UniversityForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UniversityForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = University
        fields = '__all__'
