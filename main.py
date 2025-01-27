from bs4 import BeautifulSoup
import requests


with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


div = soup.find('div', class_ = 'article')
print(div.text)

heading = div.h2.a
print(heading.text)




