
from django.db import models
from .validators import NumberValidator


class SortedArray(models.Model):
    objects = None
    array_name = models.CharField(max_length=100,  error_messages={
                                'required': 'array name must be filled'})
    array = models.TextField(default=None)
    sorted_array = models.TextField(error_messages={
                                'required': 'array must be filled'})

    def __str__(self):
        return self.array_name

