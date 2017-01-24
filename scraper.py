import re
from bs4 import BeautifulSoup
from requests import get
from json import dump


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
        'link': a.attrs['href'],
        'models': {}
    }

# zbieranie linkow do konkretnych modeli; zapisywane w phones[marka][models]
for brand in phones.keys():
    print('Zbieranie informacji o modelach telefonów marki {}...'.format(brand))

    # pobieranie calej strony marki
    url = SITE_URL + phones[brand]['link']
    while True:
        brand_site = get(url).text
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
        try:
            is_next = False
            lis = brand_site_soup.find_all('li', {'class': 'arrow'})  # [-1].select_one('a').attrs['href']
            for li in lis:
                if 'unavailable' not in li.attrs['class']:
                    url = SITE_URL + li.select_one('a').attrs['href']
                    is_next = True
            if not is_next:
                break
            print(url)
        except IndexError:
            break


# zbieranie danych o konkretnych modelach
for brand in list(phones.keys()):
    for model in phones[brand]['models']:
        print('Zbieranie informacji o telefonie {} {}...'.format(brand, model))

        model_site = get(phones[brand]['models'][model]['link']).text
        model_site_soup = BeautifulSoup(model_site, 'html.parser')

        searched_text_spec = ['Standard GSM', 'Waga', 'Standardowa bateria', 'Wyświetlacz', 'Ochrona wyświetlacza',
                              'Pamięć wbudowana', 'Pamięć RAM', 'System operacyjny', 'Procesor',
                              'Wprowadzony na rynek', 'Szybkie ładowanie', 'Ekran dotykowy', 'Akcelerometr',
                              'Zbliżeniowy', 'Światła', 'Magnetometr', 'Żyroskop', 'Barometr', 'Wysokościomierz',
                              'Grawitacyjny', 'Skaner tęczówki', 'Czytnik linii papilarnych', 'Termometr', 'Higrometr']
        for spec in searched_text_spec:
            try:
                phones[brand]['models'][model][spec] = model_site_soup.find('div', text=re.compile(spec))\
                                                        .parent.select_one('.phoneCategoryValue').text.strip().rstrip()
            except AttributeError:
                phones[brand]['models'][model][spec] = ''

        searched_tick_spec = ['Ekran dotykowy', 'Szybkie ładowanie', 'Akcelerometr', 'Zbliżeniowy', 'Światła',
                              'Magnetometr', 'Żyroskop', 'Barometr', 'Wysokościomierz', 'Grawitacyjny',
                              'Skaner tęczówki', 'Czytnik linii papilarnych', 'Termometr', 'Higrometr']
        for spec in searched_tick_spec:
            if not phones[brand]['models'][model][spec]:
                try:
                    phones[brand]['models'][model][spec] = model_site_soup.find('div', text=re.compile(spec)) \
                        .parent.select_one('.phoneCategoryValue').find('span')['class'][0]
                except (AttributeError, TypeError):
                    phones[brand]['models'][model][spec] = None

# usuwanie 'PL' z modeli
to_remove = []
for brand in phones.keys():
    for model in phones[brand]['models']:
        if model == 'PL':
            to_remove.append((brand, model))

for brand, model in to_remove:
    del phones[brand]['models'][model]


for brand in phones.keys():
    for model in phones[brand]['models']:
        # oczyszczanie inforacji o baterii z 'Kup Power Bank'
        batery_info = phones[brand]['models'][model]['Standardowa bateria']
        try:
            phones[brand]['models'][model]['Standardowa bateria'] = int(batery_info.split(' ')[1:2][0])
        except ValueError:
            phones[brand]['models'][model]['Standardowa bateria'] = None

        # zamienia tick/cross na True/False
        tick_cross = ['Akcelerometr', 'Zbliżeniowy', 'Światła', 'Magnetometr', 'Żyroskop', 'Barometr',
                      'Wysokościomierz', 'Grawitacyjny', 'Skaner tęczówki', 'Czytnik linii papilarnych',
                      'Termometr', 'Higrometr', 'Ekran dotykowy']
        for feature in tick_cross:
            prop = phones[brand]['models'][model][feature]
            if prop == 'tick':
                phones[brand]['models'][model][feature] = True
            elif prop == 'cross':
                phones[brand]['models'][model][feature] = False

        fast_charge = phones[brand]['models'][model]['Szybkie ładowanie']
        if fast_charge == 'tick' or (fast_charge and not fast_charge == 'cross'):
            phones[brand]['models'][model]['Szybkie ładowanie'] = True
        elif fast_charge == 'cross':
            phones[brand]['models'][model]['Szybkie ładowanie'] = False

        # oczyszczenie wagi
        weight = phones[brand]['models'][model]['Waga']
        try:
            phones[brand]['models'][model]['Waga'] = float(weight.split(' ')[:1][0])
        except ValueError:
            phones[brand]['models'][model]['Waga'] = None

        # oczyszczenie pamieci ram
        ram = phones[brand]['models'][model]['Pamięć RAM']
        try:
            phones[brand]['models'][model]['Pamięć RAM'] = int(ram.split(' ')[0])
        except ValueError:
            phones[brand]['models'][model]['Pamięć RAM'] = None

        # oczyszczenie pamieci wbudowanej
        mem = phones[brand]['models'][model]['Pamięć wbudowana']
        try:
            phones[brand]['models'][model]['Pamięć wbudowana'] = int(mem.split(' ')[0])
        except ValueError:
            phones[brand]['models'][model]['Pamięć wbudowana'] = None

# zliczanie o ilu telefonach pobrano dane
phones_count = 0
for brand in phones.keys():
    for model in phones[brand]['models']:
        phones_count += 1
print('Zebrano dane o {} telefonach'.format(phones_count))

# zapisywanie informacji o telefonach do pliku
dump(phones, open('data/phones.json', 'w'))


operating_systems = set()
create_date = set()
display_protection = set()
for brand in phones.keys():
    for model in phones[brand]['models']:
        operating_systems.add(phones[brand]['models'][model]['System operacyjny'])
        create_date.add(phones[brand]['models'][model]['Wprowadzony na rynek'])
        display_protection.add(phones[brand]['models'][model]['Ochrona wyświetlacza'])

print('Systemy operacyjne: {}'.format(operating_systems))
print('Wprowadzony na rynek: {}'.format(create_date))
dump(list(operating_systems), open('data/systemy_operacyjne.json', 'w'))
dump(list(create_date), open('data/daty_wypuszczenia.json', 'w'))
dump(list(display_protection), open('data/ochrony wyświetlacza.json', 'w'))





