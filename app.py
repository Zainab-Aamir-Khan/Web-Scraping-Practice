from bs4 import BeautifulSoup
import requests

url = requests.get('https://books.toscrape.com/').text
soup = BeautifulSoup(url, 'lxml')

products = soup.find('ol', class_ = 'row')

#scraping all the headings/title of the books
content = soup.find('body')
heading = content.find_all('h3')
for headings in heading:
    allHeadings = headings.text
    print(allHeadings)


# bookItems = products.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
# for bookTitle in bookItems:
#     book = bookTitle.h3.a['title']
#     print(book)


#scraping all the prices of the books
price = content.find_all('p', class_ = 'price_color')
for prices in price:
    allPrices = prices.text
    print(allPrices)


#scraping the status of stock
stock = content.find_all('p', class_ = 'instock availability')
for stocks in stock:
    allStocks = stocks.text.strip()
    print(allStocks)


#scraping the form status
form = content.find_all('button', class_ = 'btn btn-primary btn-block')
for forms in form:
    print(forms.text)
