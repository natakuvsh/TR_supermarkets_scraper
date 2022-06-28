from utils import webdriver,file
import shops_selenium
import shops_bs4

search_input = input('What are you looking for?(Please use english letters only): ').lower()

filename = file.generate_filename(search_term=search_input.lower())
file.save_data_to_csv(None, filename=filename, new_file=True)
print(f'File {filename} is created')


url_a101 = webdriver.generate_url(search_term=search_input, site='A101')
shops_bs4.a101_search(url=url_a101, filename=filename, search_term=search_input)
print(f'Uploaded data from A101 to {filename}')

url_carrefour = webdriver.generate_url(search_term=search_input, site='Carrefour')
shops_bs4.carrefour_search(url=url_carrefour, filename=filename, search_term=search_input)
print(f'Uploaded data from Carrefour to {filename}')


driver = webdriver.start_driver()

url_migros = webdriver.generate_url(search_term=search_input, site='Migros')
shops_selenium.migros_search(url=url_migros, driver=driver , filename=filename, search_term=search_input)
print(f'Uploaded data from Migros to {filename}')

url_sok = webdriver.generate_url(search_term=search_input, site='Sok')
shops_selenium.sok_search(url=url_sok, driver=driver , filename=filename, search_term=search_input)
print(f'Uploaded data from Sok to {filename}')

driver.quit()
