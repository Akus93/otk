from owlready import *
import os

path = '/'.join(os.path.realpath(__file__).split('/')[:-1]) + '/data'
onto = Ontology("new_onto.owl")
onto_path.append(path)


class Smartphone(Thing):
    ontology = onto


class Brand(Thing):
    ontology = onto


class Model(Thing):
    ontology = onto


class HaveBrand(Property):
    ontology = onto
    domain = [Smartphone]
    range = [Brand]


class HaveModel(Property):
    ontology = onto
    domain = [Brand]
    range = [Model]


class HaveGSMStandard(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveWeight(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [float]


class HaveBattery(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [int]


class HaveScreen(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveScreenProtection(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveMemory(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [int]


class HaveRAM(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [int]


class HaveOperatingSystem(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveProcessor(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveYearOfIntro(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveQuickCharge(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [bool]


my_phone = Smartphone("my_phone")
nokia = Brand("Nokia")
lumia6 = Model("Lumia_600")
lumia7 = Model("Lumia_700")
# gsm = GSMStandard("600/900")
# weight = Weight("600 g")
# battery = Battery("2000 mAh")

my_phone.HaveBrand.append(nokia)
nokia.HaveModel.append(lumia6)
nokia.HaveModel.append(lumia7)
# lumia6.HaveGSMStandard.append(gsm)
# lumia6.HaveWeight.append(weight)
# lumia6.HaveBattery.append(battery)
# lumia7.HaveGSMStandard.append(gsm)
# lumia7.HaveWeight.append(weight)
# lumia7.HaveBattery.append(battery)

lumia6.HaveGSMStandard = "600/900"
lumia6.HaveWeight = "1000"
lumia6.HaveBattery = "5000"
lumia7.HaveGSMStandard = "600/900"
lumia7.HaveWeight = "600"
lumia7.HaveBattery = "2000"

print(my_phone.HaveBrand)
print(nokia.HaveModel)
print(lumia7.HaveBattery)
print(my_phone)


onto.save()
