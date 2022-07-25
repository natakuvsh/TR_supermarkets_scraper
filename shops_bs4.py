from utils import file
from utils.regex_matcher import regex_match
from bs4 import BeautifulSoup
import requests



headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
           "Accept-Encoding": "gzip, deflate",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
           "Connection": "close", "Upgrade-Insecure-Requests": "1"}


def a101_search(url, filename, search_term):
    r = requests.get(url, headers=headers)
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    for d in soup.findAll('li', attrs={'col-md-4 col-sm-6 col-xs-6 set-product-item'}):
        try:
            product = d.find('h3', attrs={'class':'name'})
            price_with_tl = d.find('span', attrs={'class': 'current'})
            price_commas = price_with_tl.text.replace("₺", "")
            price = price_commas.replace(",",".")
            record = regex_match(product=product.text, price=price, site='A101', search_term=search_term)
            if record:
                file.save_data_to_csv(record, filename)
            else:
                pass
        except AttributeError:
            pass

def carrefour_search(url, filename, search_term):
    r = requests.get(url, headers=headers)
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    for d in soup.findAll('li', attrs={'col-xs-4 col-sm-3 col-md-3 col-lg-2 product-listing-item'}):
        price_full = d.find('span', attrs={'class': 'item-price js-variant-discounted-price'})
        try:
            price_text = price_full.text
            price_commas = price_text.replace("TL", "")
            price = price_commas.replace(",", ".")
            product = d.find('span', attrs={'class': 'item-name'})
            record = regex_match(product=product.text, price=price, site='Carrefour', search_term=search_term)
            if record:
                file.save_data_to_csv(record=record, filename=filename)
            else:
                pass
        except AttributeError:
            pass
