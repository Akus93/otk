import re
from bs4 import BeautifulSoup
from requests import get
from json import dump
from time import sleep

from pprint import pprint

from owlready import *

onto = Ontology("onto.owl")
onto_path.append("/home/ania/PycharmProjects/otk/otk_pl/otk_pl")


class Smartphone(Thing):
    ontology = onto


class Brand(Smartphone):
    ontology = onto


class Model(Brand):
    ontology = onto


class HasBrandName(Property):
    ontology = onto
    domain = [Smartphone]
    range = [Brand]


class HasModel(HasBrandName):
    ontology = onto
    domain = [Brand]
    range = [Model]


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
for brand in phones.keys():
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
            } #phones_a.text - model, brand = brand,


            Smartphone(phone_a.attrs['alt']).HasBrandName.append(Brand(brand))
            Brand(brand).HasModel.append(Model(phone_a.text))


onto.save()
print(onto.instances)


# zbieranie danych o konkretnych modelach
for brand in list(phones.keys())[:3]:
    for model in phones[brand]['models']:
        print('Zbieranie informacji o telefonie {} {}...'.format(brand, model))
        sleep(0.5)
        print(phones[brand]['models'][model]['link'])

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

# usuwanie 'PL' z modeli
to_remove = []
for brand in phones.keys():
    for model in phones[brand]['models']:
        if model == 'PL':
            to_remove.append((brand, model))

for brand, model in to_remove:
    del phones[brand]['models'][model]

pprint(phones)

# oczyszczanie inforacji o baterii z 'Kup Power Bank'
for brand in phones.keys():
    for model in phones[brand]['models']:
        batery_info = phones[brand]['models'][model]['Standardowa bateria']
        phones[brand]['models'][model]['Standardowa bateria'] = batery_info.split('\\')[0]  # TODO nie rozdziela poprawnie

# zliczanie o ile telefonach pobrano dane
phones_count = 0
for brand in phones.keys():
    for model in phones[brand]['models']:
        phones_count += 1
print('Zebrano dane o {} telefonach'.format(phones_count))

# zapisywanie informacji o telefonach do pliku
dump(phones, open('data/phones.json', 'w'))




