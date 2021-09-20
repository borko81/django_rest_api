from django.db import models


class Todos(models.Model):
    name = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
