# Supermarket scraper 

Console-app which uses Selenium and BeautifulSoap libraries to scrape data from supermarkets and creates a file with product name, price, weight and price for kg.

In order to run this script you need to have some dependencies installed::
```
pip install requirements.txt
```
To run the script:
```
python3 food_price_compare.py
```

To-Do's:
- [x] Create the main structure of the project
- [x] Add bs4 for scraping A101 and Carrefour supermarkets
- [x] Add selenium for scraping Migros and Sok supermarkets
- [x] Use regex matcher to split product description into name, price and weight
- [x] Add function to calculate price for kg/l, according on unit 
- [ ] Add images to a file
- [ ] Make a gui
