day = 11
month = 4
year = 23


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


print(num_sum((day + month + year)))
