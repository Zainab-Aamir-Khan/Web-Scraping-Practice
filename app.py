from bs4 import BeautifulSoup
import requests

url = requests.get('https://books.toscrape.com/').text
soup = BeautifulSoup(url, 'lxml')

products = soup.find('ol', class_ = 'row')
content = soup.find('body')
heading = content.find_all('h3')
for headings in heading:
    allHeadings = headings.text
    print(allHeadings)


# bookItems = products.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
# for bookTitle in bookItems:
#     book = bookTitle.h3.a['title']
#     print(book)


