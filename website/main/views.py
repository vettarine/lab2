from .models import SortedArray
from django.shortcuts import render, get_object_or_404
from .forms import SortedArrayForm
from django.shortcuts import redirect
from .tests import *
from .database_work import *
from .sorting import cocktail_sort
import sqlite3


def index(request):
    array = SortedArray.objects.all()
    return render(request, 'main/index.html', {'array': array})


def tests(request):
    db_create('arrays.db')

    results = []
    flag = True
    amount = 10
    while flag:
        amount *= 10
        results.append(test_generate(amount))
        results.append(test_sort(amount))
        results.append(test_delete(amount))

        if amount == 10000:
            flag = False
    data = {"header": "Tests results", "message1": results[0], "message2": results[1], "message3": results[2],
            "message4": results[3], "message5": results[4], "message6": results[5], "message7": results[6],
            "message8": results[7], "message9": results[8]}

    return render(request, 'main/tests.html', context=data)


def post_detail(request, pk):
    post = get_object_or_404(SortedArray, pk=pk)
    return render(request, 'main/post_detail.html', {'post': post})


def error(request):
    return render(request, 'main/error.html')


def post_new(request):
    if request.method == "POST":
        form = SortedArrayForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            item_id = post.pk

            array = form.cleaned_data['sorted_array']

            for i in array:
                if i not in '0123456789 ':
                    error(request)
                    return render(request, 'main/error.html')
            post.save()
            array = array.split()
            array_tmp = []
            for a in array:
                tmp = int(a)
                array_tmp.append(tmp)
            sorted_array = cocktail_sort(array_tmp)

            list = ""
            for a in sorted_array:
                list += str(a) + " "
            list = list[:-1]

            con = sqlite3.connect('db.sqlite3')
            cursor = con.cursor()
            cursor.execute("UPDATE main_sortedarray SET array = ? WHERE id = ?", (list, item_id))  # сиквел запрос
            con.commit()
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

            item_id = post.pk

            array = form.cleaned_data['sorted_array']

            for i in array:
                if i not in '0123456789 ':
                    error(request)
                    return render(request, 'main/error.html')

            post.save()
            array = array.split()
            array_tmp = []
            for a in array:
                tmp = int(a)
                array_tmp.append(tmp)
            sorted_array = cocktail_sort(array_tmp)

            list = ""
            for a in sorted_array:
                list += str(a) + " "
            list = list[:-1]

            con = sqlite3.connect('db.sqlite3')
            cursor = con.cursor()
            cursor.execute("UPDATE main_sortedarray SET array = ? WHERE id = ?", (list, item_id))  # сиквел запрос
            con.commit()
            return redirect('post_detail', pk=post.pk)
    else:
        form = SortedArrayForm(instance=post)
    return render(request, 'main/post_edit.html', {'form': form})
