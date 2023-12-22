from django import forms

from .models import SortedArray


class SortedArrayForm(forms.ModelForm): #задаем форму

    class Meta:
        model = SortedArray
        fields = ('array_name', 'array', 'sorted_array')
