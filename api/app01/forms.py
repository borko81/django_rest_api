from django import forms
from .models import University, Student


class AddBootstrap:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control'
            })


class UniversityForm(forms.ModelForm, AddBootstrap):

    class Meta:
        model = University
        fields = '__all__'


class StudentForm(forms.ModelForm, AddBootstrap):

    class Meta:
        model = Student
        fields = '__all__'
