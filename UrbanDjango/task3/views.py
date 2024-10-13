from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.template import Context


# Create your views here.

def store(requests):
    title = 'Выберите картину'
    dates = ['Картина 1', 'Картина 2', 'Картина 3', 'Картина 4']
    releases = [f'№{i} от {date}' for i, date in enumerate(dates, start=1)]
    context = {'title': title,
               'releases': releases}

    return render(requests, 'store.html', context=context)


def basket(requests):
    title = 'Вы выбрали картину!'
    name = 'Успешный выбор!'
    context = {'title':title,
               'name':name}

    return render(requests, 'basket.html', context=context)