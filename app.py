from bs4 import BeautifulSoup
import requests

url = requests.get('https://books.toscrape.com/').text
soup = BeautifulSoup(url, 'lxml')

products = soup.find('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
article = products.find('article', class_ = 'product_pod').text.strip()
clean_text = ' '.join(article.split()) 
print(clean_text)

