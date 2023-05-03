from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'index.html', context=context)


def result(request):
    if request.method == 'GET':
        birthday = request.GET.get('birthday')
        res = birthday.split('.')
        month = res[1]  # первый сверху

        if int(res[0]) > 27:  # первый слева
            day = str(int(res[0][0]) + int(res[0][1]))
        else:
            day = res[0]

        year = int(res[2][0]) + int(res[2][1]) + int(res[2][2]) + int(res[2][3])

        if int(year) > 27: # первый справа
            year = str(year)
            year = str(int(year[0]) + int(year[1]))

        formula_1 = int(day) + int(month) + int(year)  # Первый снизу
        formula_2 = formula_1 * 2  # центр
        formula_3 = int(day) + formula_2  # третий слева
        formula_4 = int(day) + formula_3  # второй слева
        formula_5 = int(month) + formula_2  # третий сверху
        formula_6 = int(month) + formula_5  # второй сверху
        formula_7 = int(year) + formula_2  # третий справа
        formula_8 = int(year) + formula_7  # второй справа
        formula_9 = formula_1 + formula_2  # третий снизу
        formula_10 = formula_1 + formula_9  # второй снизу
        formula_11 = formula_7 + formula_9  # четвертый правый-низ
        formula_12 = formula_11 + formula_9  # love
        formula_13 = formula_7 + formula_11  # money

        context = {
            'title': 'Результат',
            'birthday': birthday,
            'year': year,
            'day': day,
            'month': month,
            'formula_1': formula_1,
            'formula_2': formula_2,
            'formula_3': formula_3,
            'formula_4': formula_4,
            'formula_5': formula_5,
            'formula_6': formula_6,
            'formula_7': formula_7,
            'formula_8': formula_8,
            'formula_9': formula_9,
            'formula_10': formula_10,
            'formula_11': formula_11,
            'formula_12': formula_12,
            'formula_13': formula_13
        }
    else:
        context = {
            'title': 'Результат',
        }
    return render(request, 'result.html', context=context)
