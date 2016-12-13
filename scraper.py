import re
from bs4 import BeautifulSoup
from requests import get
from json import dump
from time import sleep

from pprint import pprint


SITE_URL = 'http://www.mgsm.pl'

phones = {}


# pobieranie calej glownej strony
main_site = get(SITE_URL).text
main_site_soup = BeautifulSoup(main_site, 'html.parser')

# uzupelnianie 'phones' markami telefonow i linkami do kazdej z nich
brand_ul = main_site_soup.select_one('.Brands')
for brand in brand_ul.select('li'):
    a = brand.select_one('a')
    phones[a.text] = {
        'link': SITE_URL + a.attrs['href'],
        'models': {}
    }

# zbieranie linkow do konkretnych modeli; zapisywane w phones[marka][models]
for brand in list(phones.keys())[:3]:
    print('Zbieranie informacji o modelach telefonów marki {}...'.format(brand))

    # pobieranie calej strony marki
    brand_site = get(phones[brand]['link']).text
    brand_site_soup = BeautifulSoup(brand_site, 'html.parser')

    wrap_container = brand_site_soup.select_one('.wrapContainer')
    phone_list_li = wrap_container.select('.phone-small-box-list')
    for phone_li in phone_list_li:
        phone_a = phone_li.select_one('a')
        # zapisywanie modelu telefonu i linku do niego
        if not phone_a.attrs['href'] == SITE_URL:
            phones[brand]['models'][phone_a.text] = {
                'link': SITE_URL + phone_a.attrs['href']
            }

# zbieranie danych o konkretnych modelach
for brand in phones.keys():
    for model in phones[brand]['models']:
        print('Zbieranie informacji o telefonie {} {}...'.format(brand, model))
        sleep(0.5)
        model_site = get(phones[brand]['models'][model]['link']).text
        model_site_soup = BeautifulSoup(model_site, 'html.parser')

        searched_spec = ['Standard GSM', 'Waga', 'Standardowa bateria', 'Wyświetlacz', 'Ochrona wyświetlacza',
                         'Pamięć wbudowana', 'Pamięć RAM', 'System operacyjny', 'Procesor', 'Wprowadzony na rynek']
        for spec in searched_spec:
            try:
                phones[brand]['models'][model][spec] = model_site_soup.find('div', text=re.compile(spec))\
                                                        .parent.select_one('.phoneCategoryValue').text.strip().rstrip()
            except AttributeError:
                phones[brand]['models'][model][spec] = ''


# zapisywanie informacji o telefonach do pliku
dump(phones, open("phones.txt", 'w'))




