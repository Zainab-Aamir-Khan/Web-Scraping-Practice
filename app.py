from bs4 import BeautifulSoup
import requests

url = requests.get('https://books.toscrape.com/').text
soup = BeautifulSoup(url, 'lxml')

products = soup.find('ol', class_ = 'row')


book = products.find('h3').a['title']
print(book)


