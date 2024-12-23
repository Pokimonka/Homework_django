import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


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
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    offset = datetime.timedelta(hours=3)
    tz = datetime.timezone(offset, name='МСК')
    current_time = datetime.datetime.now(tz=tz).time()
    print(datetime.datetime.now())
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    dir = '../first_project/app'
    files_and_dirs = os.listdir(dir)
    files = [file for file in files_and_dirs if '.' in file]
    dirs = [directory for directory in files_and_dirs if '.' not in directory]
    msg = (f'Файлы в рабочей директории: {files} <br>'
           f'Папки в рабочей директории: {dirs} </br>')
    return HttpResponse(msg)
