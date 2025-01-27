from bs4 import BeautifulSoup
import requests

url = requests.get('https://books.toscrape.com/').text
soup = BeautifulSoup(url, 'lxml')

products = soup.find_all('li')
print(products)