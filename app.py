from bs4 import BeautifulSoup
import requests

url = requests.get('https://books.toscrape.com/')
soup = BeautifulSoup('html_file', 'lxml')