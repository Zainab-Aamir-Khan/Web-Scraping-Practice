from bs4 import BeautifulSoup
import requests


with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


mainTitle = soup.find_all('div', class_ = 'article')
    
print(mainTitle.text)


