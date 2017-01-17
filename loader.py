import json
from pprint import pprint

#
# class Phone:
#     def __init__(self, phone_dict):
#         self.brand = phone_dict['maker']['name']
#         self.model = phone_dict['name']['id']
#         self.cpu_name = phone_dict['cpu']['name']
#         self.cpu_freq = phone_dict['cpu']['freq']
#         self.cpu_cores = phone_dict['cpu']['cores']
#         self.display_height = phone_dict['display']['h']
#         self.display_width = phone_dict['display']['w']
#         self.display_size = phone_dict['display']['s']
#         self.ram = phone_dict['memory']['ram']
#         self.memory = phone_dict['memory']['ram']
#         self.system_name = phone_dict['os'].get('type', None)
#         self.system_version = phone_dict['os']['ver']
#
#     def __str__(self):
#         return '{} {}'.format(self.brand, self.model)
#
#
# with open('data/devices.json') as data_file:
#     data = json.load(data_file)
#
#
# for key in data.keys():
#     phones.append(Phone(phone_dict=data[key]))

# for phone in phones:
#     print(phone)

attributes = ['Standard GSM', 'Waga', 'Standardowa bateria', 'Wyświetlacz', 'Ochrona wyświetlacza', 'Pamięć wbudowana',
              'Pamięć RAM', 'System operacyjny', 'Procesor', 'Wprowadzony na rynek', 'Szybkie ładowanie',
              'Ekran dotykowy', 'Akcelerometr', 'Zbliżeniowy', 'Światła', 'Magnetometr', 'Żyroskop', 'Barometr',
              'Wysokościomierz', 'Grawitacyjny', 'Skaner tęczówki', 'Czytnik linii papilarnych', 'Termometr',
              'Higrometr']

with open('data/phones.json') as data_file:
    data = json.load(data_file)

for brand in data.keys():
    print(brand)
    for model in data[brand]['models']:
        print(model)
        print(data[brand]['models'][model]['Standard GSM'])
        print(data[brand]['models'][model]['Waga'])
        print(data[brand]['models'][model]['Standardowa bateria'])
        print(data[brand]['models'][model]['Wyświetlacz'])
        print(data[brand]['models'][model]['Ochrona wyświetlacza'])
        print(data[brand]['models'][model]['Pamięć wbudowana'])
        print(data[brand]['models'][model]['Pamięć RAM'])
        print(data[brand]['models'][model]['System operacyjny'])
        print(data[brand]['models'][model]['Procesor'])
        print(data[brand]['models'][model]['Wprowadzony na rynek'])
        print(data[brand]['models'][model]['Szybkie ładowanie'])
        print(data[brand]['models'][model]['Ekran dotykowy'])
        print(data[brand]['models'][model]['Akcelerometr'])
        print(data[brand]['models'][model]['Zbliżeniowy'])
        print(data[brand]['models'][model]['Światła'])
        print( data[brand]['models'][model]['Magnetometr'])
        print(data[brand]['models'][model]['Żyroskop'])
        print(data[brand]['models'][model]['Barometr'])
        print(data[brand]['models'][model]['Wysokościomierz'])
        print(data[brand]['models'][model]['Grawitacyjny'])
        print(data[brand]['models'][model]['Skaner tęczówki'])
        print(data[brand]['models'][model]['Czytnik linii papilarnych'])
        print(data[brand]['models'][model]['Termometr'])
        print(data[brand]['models'][model]['Higrometr'])



