from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('result/', result, name='result'),
    path('second_variable/', second, name='second'),
    path('second_variable/result', result_2, name='result_2')
]