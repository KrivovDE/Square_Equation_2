import math

from django.shortcuts import render
from .forms import UserForm


def start(request):
    """Для определения типа запроса проверяем значение request.method"""
    if request.method == 'POST':
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        c = float(request.POST.get('c'))

        """Проверяем что а != 0, иначе будет ошибка деления на 0"""
        if a == 0:
            x = 'Уравнение не имеет решений, так как возникает ошибка "Zero Division Error",' \
                ' убедитесь что введенное значение "а" не равно 0'
            return render(request, 'finish.html', {'a': a, 'b': b, 'c': c, 'x': x})
        else:
            """Считаем дискриминант и в зависимости от этого, применяем формулу"""
            D = b ** 2 - 4 * a * c
            if D > 0:
                x1 = (-b + math.sqrt(D)) / (2 * a)
                x2 = (-b - math.sqrt(D)) / (2 * a)
                return render(request, 'finish.html', {'a': a, 'b': b, 'c': c, 'D': D, 'x1': x1, 'x2': x2})
            elif D == 0:
                x3 = (-b + math.sqrt(D)) / (2 * a)
                return render(request, 'finish.html', {'a': a, 'b': b, 'c': c, 'D': D, 'x3': x3})
            else:
                x4 = 'Уравнение не имеет решений'
                return render(request, 'finish.html', {'a': a, 'b': b, 'c': c, 'D': D, 'x4': x4})
    else:
        """Здесь объект формы передается в шаблон start.html в виде переменной form"""
        userform = UserForm()
        return render(request, 'start.html', {'form': userform})
