from selenium import webdriver

def start_driver():
    """
    Starting the web driver
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(r'C:\Users\Natali\Downloads\chromedriver.exe', options=options)
    return driver


def generate_url(search_term, site):
    """
    Generating the search url
    """
    if site == 'Migros':
        base_template = 'https://www.migros.com.tr/arama?q={}'
        search_term = search_term.replace(' ', '%20')
    elif site == 'Sok':
        base_template = 'https://www.sokmarket.com.tr/arama/{}'
        search_term = search_term.replace(' ', '%20')
    elif site == 'A101':
        base_template = 'https://www.a101.com.tr/list/?search_text={}'
        search_term = search_term.replace(' ', '%20')
    elif site == 'Carrefour':
        base_template = 'https://www.carrefoursa.com/search?q={}&show=All'
        search_term = search_term.replace(' ', '+')
    else:
        print('Could not generate url')
    stem = base_template.format(search_term)
    return stem

