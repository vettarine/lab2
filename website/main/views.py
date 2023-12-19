from django.http import JsonResponse
from .models import SortedArray
from django.shortcuts import render, get_object_or_404
from .forms import SortedArrayForm
from django.shortcuts import redirect
# from sorting import cocktail_sort ИМПОРТ ФУНКЦИИ ШЛЕТ


def index(request):
    array = SortedArray.objects.all() # класс сортед аррей починить
    return render(request, 'main/index.html', {'array': array})


def sort_array(request):
    if request.method == 'POST':
        form = SortedArrayForm(request.POST)
        if form.is_valid():
            if 'action' in request.POST:
                array_name = form.cleaned_data['array_name']
                sorted_array = form.cleaned_data['sorted_array']
                # sorted_array = ВОТ ЗДЕСЬ ФУНКЦИЯ СОРТИРОВКИ

                # Логика сохранения данных
                print(array_name)
                print(sorted_array)

        return JsonResponse({'sorted_array': sorted_array})

    return JsonResponse({'error': 'Invalid request'})


def post_detail(request, pk):
    post = get_object_or_404(SortedArray, pk=pk)
    return render(request, 'main/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = SortedArrayForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = SortedArrayForm()
    return render(request, 'main/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(SortedArray, pk=pk)
    if request.method == "POST":
        form = SortedArrayForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = SortedArrayForm(instance=post)
    return render(request, 'main/post_edit.html', {'form': form})
