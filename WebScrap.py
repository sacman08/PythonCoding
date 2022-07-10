import requests
from bs4 import BeautifulSoup

# TODO examine BeautifulSoup website for how to use
# Make a request to a URL
# Store the result in 'res' variable

res = requests.get('https://www.twitter.com/')

soup = BeautifulSoup(res.content, 'html.parser')
page_title = soup.title.text
page_body = soup.body.text
page_head = soup.head.text


print(page_head, page_body)
