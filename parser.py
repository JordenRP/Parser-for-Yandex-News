import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)#Запрос страницы
    return response.text# Возвращение HTML кода


def get_news(html):
    soup = BeautifulSoup(html, 'lxml')
    spans = soup.find('ol', class_='news__list').findAll('span', class_='news__item-content') #Поиск первых четрыех строк
    span_last = soup.find('ol', class_='news__animation-list').find('span', class_='news__item-content') #Поиск пятой анимированной строки

    news = []
    
    for s in spans:
        news.append(s.get_text())

    news.append(span_last.get_text())
     
    return news


def main():
    url = 'https://yandex.ru/'
    all_news = get_news(get_html(url))
    with open('news.txt', 'w') as file:
        for line in all_news:
            file.write(line+'\n')

main()
