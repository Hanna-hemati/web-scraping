from bs4 import BeautifulSoup
import requests

url = ("https://webscraper.io/test-sites/e-commerce/allinone")
page_request = requests.get(url).text
soup = BeautifulSoup(page_request, 'html.parser')
card = soup.findAll('p', attrs = {"class" : "description card-text"})
for cards in card:
    print(cards.text)
