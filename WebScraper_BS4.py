# TODO join in a class to allow encapsulation

from bs4 import BeautifulSoup
import requests
import re

url = "http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')


def find_item_name():
    locater = 'article.product_pod h3 a'
    item_link = soup.select(locater)
    for each_link in item_link:
        item_name = each_link.attrs['title']
        # What do we want to do with the titles??
        print(item_name)


def find_pricing():
    paragraph_contents = soup.find_all('p', attrs={"class": "price_color"})
    price_pattern = '([0-9]+\.[0-9]+)'
    for each_price in paragraph_contents:
        each_price = each_price.string
        price_matching = re.search(price_pattern, each_price)
        print(float(price_matching.group(0)))


find_item_name()
find_pricing()
