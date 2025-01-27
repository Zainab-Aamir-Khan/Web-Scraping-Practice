from bs4 import BeautifulSoup
import requests


with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


for div in soup.find_all('div', class_ = 'article'):
# print(div.text)

    heading = div.h2.a.text
    print(heading)

    para = div.p.text
    print(para)

    print()








