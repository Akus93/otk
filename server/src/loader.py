import json
import ontology as onto

with open('../data/phones.json') as data_file:
    data = json.load(data_file)

phone = onto.Smartphone("smartphone")

for brand in data.keys():
    onto_brand = onto.Brand(brand.replace(" ", "_"))
    phone.HaveBrand.append(onto_brand)
    for model in data[brand]['models']:
        onto_model = onto.Model(model.replace(" ", "_"))
        onto_brand.HaveModel.append(onto_model)
        onto_model.HaveGSMStandard = data[brand]['models'][model]['Standard GSM'].replace(" ", "_")
        onto_model.HaveWeight = data[brand]['models'][model]['Waga']
        onto_model.HaveBattery = data[brand]['models'][model]['Standardowa bateria']
        onto_model.HaveScreen = data[brand]['models'][model]['Wyświetlacz'].replace(" ", "_")
        onto_model.HaveScreenProtection = data[brand]['models'][model]['Ochrona wyświetlacza'].replace(" ", "_")
        onto_model.HaveMemory = data[brand]['models'][model]['Pamięć wbudowana']
        onto_model.HaveRAM = data[brand]['models'][model]['Pamięć RAM']
        onto_model.HaveOperatingSystem = data[brand]['models'][model]['System operacyjny'].replace(" ", "_")
        onto_model.HaveProcessor = data[brand]['models'][model]['Procesor'].replace(" ", "_")
        onto_model.HaveYearOfIntro = data[brand]['models'][model]['Wprowadzony na rynek'].replace(" ", "_")
        onto_model.HaveQuickCharge = str(data[brand]['models'][model]['Szybkie ładowanie'])
        onto_model.HaveTouchScreen = str(data[brand]['models'][model]['Ekran dotykowy'])
        onto_model.HaveAccelerometer = str(data[brand]['models'][model]['Akcelerometr'])
        onto_model.HaveProximitySensor = str(data[brand]['models'][model]['Zbliżeniowy'])
        onto_model.HaveLightSensor = str(data[brand]['models'][model]['Światła'])
        onto_model.Magnetometer = str(data[brand]['models'][model]['Magnetometr'])
        onto_model.HaveGyroscope = str(data[brand]['models'][model]['Żyroskop'])
        onto_model.HaveBarometer = str(data[brand]['models'][model]['Barometr'])
        onto_model.HaveAltimeter = str(data[brand]['models'][model]['Wysokościomierz'])
        onto_model.HaveGravitySensor = str(data[brand]['models'][model]['Grawitacyjny'])
        onto_model.HaveIrisScanner = str(data[brand]['models'][model]['Skaner tęczówki'])
        onto_model.HaveFingerprintScanner = str(data[brand]['models'][model]['Czytnik linii papilarnych'])
        onto_model.HaveThermometer = str(data[brand]['models'][model]['Termometr'])
        onto_model.HaveHygrometer = str(data[brand]['models'][model]['Higrometr'])

onto.onto.save()
