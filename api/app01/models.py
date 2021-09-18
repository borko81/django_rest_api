from django.db import models


class University(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Universitiy'
        verbose_name_plural = 'Universities'

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Strudent'
        verbose_name_plural = 'Students'

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
