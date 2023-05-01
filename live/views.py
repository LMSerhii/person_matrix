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
        month = res[1]

        if int(res[0]) > 27:
            day = str(int(res[0][0]) + int(res[0][1]))
        else:
            day = res[0]

        year = int(res[2][0]) + int(res[2][1]) + int(res[2][2]) + int(res[2][3])

        if int(year) > 27:
            year = str(year)
            year = str(int(year[0]) + int(year[1]))

        context = {
            'title': 'Результат',
            'birthday': birthday,
            'year': year,
            'day': day,
            'month': month
        }
    else:
        context = {
            'title': 'Результат',
        }
    return render(request, 'result.html', context=context)
