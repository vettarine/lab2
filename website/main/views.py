from django.http import JsonResponse
from .models import SortedArray
from django.shortcuts import render, get_object_or_404
from .forms import SortedArrayForm
from django.shortcuts import redirect
# from sorting import cocktail_sort ИМПОРТ ФУНКЦИИ ШЛЕТ

def cocktail_sort(sort_array):
    """Sort with cocktail sort method and return the array"""
    length = len(sort_array) # длина массива
    for i in range(length - 1, 0, -1):
        is_swapped = False  # цикл идет, пока элементы меняются местами (т.е. пока не стоят в нужном порядке)

        for j in range(i, 0, -1):  # сортировка с конца массива (меньший элемент к началу массива)
            if sort_array[j] < sort_array[j - 1]:
                sort_array[j], sort_array[j - 1] = sort_array[j - 1], sort_array[j]
                is_swapped = True  # элементы меняли местами или нет?

        for j in range(i):  # сортировка с начала массива (больший элемент к концу массива)
            if sort_array[j] > sort_array[j + 1]:
                sort_array[j], sort_array[j + 1] = sort_array[j + 1], sort_array[j]
                is_swapped = True  # элементы меняли местами или нет?

        if not is_swapped:  # если элементы не переставляли (все элементы в нужном порядке)
            return sort_array


def index(request):
    array = SortedArray.objects.all()
    return render(request, 'main/index.html', {'array': array})


def sort_array(request):
    if request.method == 'POST':
        form = SortedArrayForm(request.POST)
        if form.is_valid():
            if 'action' in request.POST:
                array_name = form.cleaned_data['array_name']
                sorted_array = form.cleaned_data['sorted_array']
                array_tmp = []
                for a in sorted_array:
                    tmp = int(a)
                    array_tmp.append(str(tmp))
                sorted_array = cocktail_sort(array_tmp)
                # Логика сохранения данных
                print(array_name)
                print(sorted_array)

        return JsonResponse({'sorted_array': sorted_array})  # класс сортед аррей починить

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
