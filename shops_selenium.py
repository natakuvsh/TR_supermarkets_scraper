from utils import file
from utils.regex_matcher import regex_match
from selenium.common import exceptions
from selenium.webdriver.common.by import By

def migros_search(url, driver, filename, search_term):
    driver.get(url)
    products = driver.find_elements(by=By.XPATH, value='/html/body/sm-root/div/main/sm-product/article/sm-list/div[2]/div[4]/div[2]/div[4]/sm-list-page-item')

    for product in products:
        try:
            price_with_tl = product.find_element(by=By.XPATH,
                                                 value=".//mat-card/div[2]/fe-product-price/div/div/span").text.strip()
            price_commas = price_with_tl.replace(" TL", "")
            price = price_commas.replace(",", ".")
        except exceptions.NoSuchElementException:
            pass
        try:
            if len(price) <= 7:
                try:
                    product_name = product.find_element(by=By.XPATH, value=".//mat-card/div[1]/a").text.strip()
                    record = regex_match(product=product_name, price=price, site='Migros', search_term=search_term)
                    if record:
                        file.save_data_to_csv(record, filename)
                except exceptions.NoSuchElementException:
                    pass
        except UnboundLocalError:
            pass

def sok_search(url, driver, filename, search_term):
    driver.get(url)
    products = driver.find_elements(by=By.XPATH, value='//*[@id="root"]/section/main/div/div/ul/li')
    for product in products:
        try:
            price_full = product.find_element(by=By.XPATH, value=".//div/a/div[2]/div/span").text.strip()
            price = price_full.replace(",",".")
        except exceptions.NoSuchElementException:
            pass
        if len(price) <= 7:
            try:
                product_name = product.find_element(by=By.XPATH, value=".//div/a/div[2]/strong").text.strip()
                record = regex_match(product=product_name,price=price,site='Sok', search_term=search_term)
                if record:
                    file.save_data_to_csv(record, filename)
            except exceptions.NoSuchElementException:
                pass

