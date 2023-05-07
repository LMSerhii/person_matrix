from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'index.html', context=context)


def result(request):
    def num_sum(num):
        num = int(num)
        if num > 27:
            return num_sum(sum(map(int, list(str(num)))))
        return num

    if request.method == 'GET':
        birthday = request.GET.get('birthday')

        res = birthday.split('.')
        month = num_sum(res[1])  # первый сверху
        day = num_sum(res[0])  # первый слева
        year = num_sum(res[1])  # первый справа
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

        f_14 = num_sum((day + f_1))  # первый левый-низ
        f_15 = num_sum((year + f_1))  # первый правый-низ
        f_16 = num_sum((year + month))  # первый правый-верх
        f_17 = num_sum((day + month))  # первый левый-верх

        f_18 = num_sum((f_2 + f_14))  # третий левый-низ
        f_19 = num_sum((f_18 + f_14))  # второй левый-низ

        f_20 = num_sum((f_2 + f_15))  # третий правый-низ
        f_21 = num_sum((f_20 + f_15))  # второй правый-низ

        f_22 = num_sum((f_2 + f_16))  # третий правый-верх
        f_23 = num_sum((f_22 + f_16))  # второй правый-верх

        f_24 = num_sum((f_2 + f_17))  # третий левый-верх
        f_25 = num_sum((f_24 + f_17))  # второй левый-верх

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
            'f_13': f_13,
            'f_14': f_14,
            'f_15': f_15,
            'f_16': f_16,
            'f_17': f_17,
            'f_18': f_18,
            'f_19': f_19,
            'f_20': f_20,
            'f_21': f_21,
            'f_22': f_22,
            'f_23': f_23,
            'f_24': f_24,
            'f_25': f_25,
        }
    else:
        context = {
            'title': 'Результат',
        }
    return render(request, 'result.html', context=context)
