from django.contrib import admin

from .models import Todos, ForTestOnly

admin.site.register(Todos)
admin.site.register(ForTestOnly)
