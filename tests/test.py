import datetime


x = '22/09/2022'

# Получение точной даты из переменной date после парсинга в виде строки
def get_time(x):
    dt = datetime.datetime.today()
    if '/' in x:
        return x
    else:
        x = int(x.strip('hours ago hour ago minutes ago minute ago < '))
        t = dt - datetime.timedelta(hours=x)
        return str(t.strftime('%d/%m/%y'))


# def get_time(x):
#     dt = datetime.datetime.today()
#     if 'hours ago' in x:
#         x = int(x.strip('hours ago <').strip())
#         t = dt - datetime.timedelta(hours=x)
#         return str(t.strftime('%d/%m/%y'))
#     if 'minutes ago' or 'minute ago' in x:
#         x = int(x.strip('minutes ago <').strip())
#         t = dt - datetime.timedelta(minutes=x)
#         return str(t.strftime('%d/%m/%y'))
#     return str(x)


print(get_time(x))
