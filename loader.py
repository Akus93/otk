import json
from pprint import pprint

phones = []


class Phone:
    def __init__(self, phone_dict):
        self.brand = phone_dict['maker']['name']
        self.model = phone_dict['name']['id']
        self.cpu_name = phone_dict['cpu']['name']
        self.cpu_freq = phone_dict['cpu']['freq']
        self.cpu_cores = phone_dict['cpu']['cores']
        self.display_height = phone_dict['display']['h']
        self.display_width = phone_dict['display']['w']
        self.display_size = phone_dict['display']['s']
        self.ram = phone_dict['memory']['ram']
        self.memory = phone_dict['memory']['ram']
        self.system_name = phone_dict['os'].get('type', None)
        self.system_version = phone_dict['os']['ver']

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)


with open('data/devices.json') as data_file:
    data = json.load(data_file)


for key in data.keys():
    phones.append(Phone(phone_dict=data[key]))

# for phone in phones:
#     print(phone)

print('Mamy {} urządzeń!'.format(len(phones)))



