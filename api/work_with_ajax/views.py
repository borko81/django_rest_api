from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework import status
from .models import Todos


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