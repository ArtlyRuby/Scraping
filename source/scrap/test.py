# from bs4 import BeautifulSoup
# import requests
# import time
# from source.models import save_house_db
# import datetime
#
#
# # Получение точной даты из переменной date после парсинга в виде строки
# def get_time(date):
#     dt = datetime.datetime.today()
#     if '/' in date:
#         return date
#     else:
#         date = int(date.strip('hours ago hour ago minutes ago minute ago < '))
#         t = dt - datetime.timedelta(hours=date)
#         return str(t.strftime('%d/%m/%y'))
#
#
# # Получение списка данных из парсинга, добавление списка данных в список
# def get_house_info(html):
#     soup = BeautifulSoup(html, 'lxml')
#     time.sleep(4)
#     houses = soup.find_all('div', class_='search-item')
#     house_data = []
#     for item in houses:
#         title = item.find(class_='title').text.strip()
#         title = title if title else "None"
#         date = item.find(class_='date-posted').text
#         date = get_time(date)
#         price = item.find(class_='price').text.strip()
#         price = price if price else "None"
#         image = item.find("img").get("data-src")
#         image = image if image else "None"
#         house_data.append([title, date, price, image])
#
#     return house_data
#
#
# def main():
#     headers = {
#         'accept': '*/*',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117'
#     }
#     page = 1
#     Pages = int(input('Введите нужное кол-во страниц для парсинга: '))
#     while page < Pages+1:
#         try:
#             url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273'
#             soup = BeautifulSoup(url, 'lxml')
#             response = requests.get(url, headers=headers)
#             html = response.text
#
#             house_data = get_house_info(html) # Сохранение данных парсинга в переменную
#             save_house_db.save_data(house_data) # Сохранение данных в БД
#
#         except:
#             raise 'Случилась неполадка'
#         finally:
#             print(f'Страница {page} прочитана...')
#             page += 1
#
#
#     print('Парсинг окончился!')
#
#
# if __name__ == "__main__":
#     main()