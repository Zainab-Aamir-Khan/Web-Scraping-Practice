from bs4 import BeautifulSoup
import requests

url = requests.get('https://books.toscrape.com/').text
soup = BeautifulSoup(url, 'lxml')

print(soup.prettify())