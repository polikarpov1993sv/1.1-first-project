from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os
def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    file = []
    rez = sorted(os.listdir("."))
    for n, item in enumerate(rez):
       filename = (n + 1, item)
       file.append(filename)
    filelist = "\n".join(str(element) for element in file)
    msg = f'Список файлов: \n {filelist}'
    return HttpResponse(msg)
