
from django.db import models


class SortedArray(models.Model):
    objects = None
    array_name = models.CharField(max_length=100)
    array = models.TextField(default=None)
    sorted_array = models.TextField()

    def __str__(self):
        return self.array_name

