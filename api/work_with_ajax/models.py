from django.db import models
from django.conf import settings


class Todos(models.Model):
    name = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class ForTestOnly(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
