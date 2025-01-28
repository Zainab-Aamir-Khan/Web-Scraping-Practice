from bs4 import BeautifulSoup
import requests
import csv

url = requests.get('https://books.toscrape.com/').text
soup = BeautifulSoup(url, 'lxml')

content = soup.find('ol', class_ = 'row')

csvFile = open('info.csv', 'w')
csvWriter = csv.writer(csvFile)


for allContent in content.find_all('li'):

    heading = allContent.h3.text
    print(heading)

    prices = allContent.find('p', class_ = 'price_color').text
    print(prices)

    stock = allContent.find('p', class_ = 'instock availability').text.strip()
    print(stock)

    form = allContent.find('button', class_ = 'btn btn-primary btn-block').text.strip()
    print(form)

    print()
