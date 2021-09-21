from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework import status
from .models import Todos
from .forms import ForForm


def check_site_is_running(request):
    return JsonResponse({'status': 'up'}, status=status.HTTP_200_OK)


def index(request):
    return render(request, 'work/index.html')


def todos(request):
    # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            todos = list(Todos.objects.all().values())
            return JsonResponse({'context': todos})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')


def form_check(request):
    form = ForForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('form_check')
    return render(request, 'work/check.html', context={'form': form})