from django.shortcuts import render


def num_sum(num):
    number = int(num)
    if 100 > number > 27:
        number = number % 10 + number // 10
    elif 1000 > number >= 100:
        number = number % 10 + (number % 100) // 10 + number // 100
    elif number >= 1000:
        number = number % 10 + (number % 100) // 10 + (number % 1000) // 100 + number // 1000
        if number > 27:
            return num_sum(number)
    return number


def index(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'index.html', context=context)


def result(request):
    if request.method == 'GET':
        birthday = request.GET.get('birthday')

        res = birthday.split('.')
        month = num_sum(res[1]) # первый сверху
        day = num_sum(res[0])
        year = num_sum(res[1])

        f_1 = num_sum((day + month + year))  # Первый снизу
        f_2 = f_1 * 2  # центр
        f_3 = num_sum((day + f_2))  # третий слева
        f_4 = num_sum((day + f_3))  # второй слева
        f_5 = num_sum((month + f_2))  # третий сверху
        f_6 = num_sum((month + f_5))  # второй сверху
        f_7 = num_sum((year + f_2))  # третий справа
        f_8 = num_sum((year + f_7))  # второй справа
        f_9 = num_sum((f_1 + f_2))  # третий снизу
        f_10 = num_sum((f_1 + f_2))  # второй снизу
        f_11 = num_sum((f_7 + f_9))  # четвертый правый-низ
        f_12 = num_sum((f_11 + f_9))  # love
        f_13 = num_sum((f_7 + f_11))  # money

        context = {
            'title': 'Результат',
            'birthday': birthday,
            'year': year,
            'day': day,
            'month': month,
            'f_1': f_1,
            'f_2': f_2,
            'f_3': f_3,
            'f_4': f_4,
            'f_5': f_5,
            'f_6': f_6,
            'f_7': f_7,
            'f_8': f_8,
            'f_9': f_9,
            'f_10': f_10,
            'f_11': f_11,
            'f_12': f_12,
            'f_13': f_13
        }
    else:
        context = {
            'title': 'Результат',
        }
    return render(request, 'result.html', context=context)
