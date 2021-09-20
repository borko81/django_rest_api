from django.shortcuts import redirect, render

from rest_framework import viewsets

from .models import University, Student
from .serializers import UniversitySerializer, StudentSerializer
from .forms import UniversityForm, StudentForm


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


def index(request):
    form = UniversityForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UniversityForm()
        return redirect('index')
    return render(request, 'app/index.html', context={'form': form})


def students(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StudentForm()
        return redirect('show_students')
    return render(request, 'app/students.html', context={'form': form})
