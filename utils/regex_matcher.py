import base64
import re
import urllib.request
import unidecode


def regex_match(product, price, site, search_term):
    pattern = '(\s*)([a-zA-ZığüşöçİĞÜŞÖÇ&; ]+)(\d+|kg)(\s*)(L|l|g|G|ml|Ml)*'
    try:
        matcher = re.search(pattern, product)
        try:
            name = matcher.group(2)
            weight = matcher.group(3)
            unit = matcher.group(5)
            """
            try:
                urllib.request.urlretrieve(image_url, f"images/{name}.jpg")
                with open(f"images/{name}.jpg", "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                    print(encoded_string.decode('utf-8'))
            except TypeError:
                pass
            """
            if search_term in unidecode.unidecode(name.lower()) or search_term.split()[0] in unidecode.unidecode(name.lower()):
                if weight.lower() == 'kg':
                    try:
                        price_kg = float(price)
                        return site, name, weight, float(price), round(price_kg,2),
                    except (ValueError,ZeroDivisionError):
                        return site, name, weight, float(price), float(price),
                elif unit.lower() == 'g' or 'ml':
                    try:
                        price_kg = 1000 * float(price) / int(weight)
                        return site, name, weight, float(price), round(price_kg,2),
                    except (ValueError, ZeroDivisionError):
                        return site, name, weight, float(price), float(price),
                elif unit.lower() == 'l':
                    try:
                        price_kg = float(price) / int(weight)
                        return site, name, weight, float(price), round(price_kg,2)
                    except (ValueError, ZeroDivisionError):
                        return site, name, weight, float(price), float(price)
        except AttributeError:
            if search_term.lower() in unidecode.unidecode(product).lower():
                return site, product, " ", float(price), " "
    except AttributeError:
        pass