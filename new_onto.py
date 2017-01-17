from owlready import *

onto = Ontology("new_onto.owl")
onto_path.append("/home/ania/PycharmProjects/otk/otk_pl/otk_pl")


class Smartphone(Thing):
    ontology = onto


class Brand(Thing):
    ontology = onto


class Model(Thing):
    ontology = onto


class GSMStandard(Thing):
    ontology = onto


class Weight(Thing):
    ontology = onto


class Battery(Thing):
    ontology = onto


class Screen(Thing):
    ontology = onto


class ScreenProtection(Thing):
    ontology = onto


class Memory(Thing):
    ontology = onto


class RAM(Thing):
    ontology = onto


class OperatingSystem(Thing):
    ontology = onto


class Processor(Thing):
    ontology = onto


class YearOfIntro(Thing):
    ontology = onto


class QuickCharge(Thing):
    ontology = onto


class HaveBrand(Property):
    ontology = onto
    domain = [Smartphone]
    range = [Brand]


class HaveModel(Property):
    ontology = onto
    domain = [Brand]
    range = [Model]


class HaveGSMStandard(Property):
    ontology = onto
    domain = [Model]
    range = [GSMStandard]


class HaveWeight(Property):
    ontology = onto
    domain = [Model]
    range = [Weight]


class HaveBattery(Property):
    ontology = onto
    domain = [Model]
    range = [Battery]


class HaveScreen(Property):
    ontology = onto
    domain = [Model]
    range = [Screen]


class HaveScreenProtection(Property):
    ontology = onto
    domain = [Model]
    range = [ScreenProtection]


class HaveMemory(Property):
    ontology = onto
    domain = [Model]
    range = [Memory]


class HaveRAM(Property):
    ontology = onto
    domain = [Model]
    range = [RAM]


class HaveOperatingSystem(Property):
    ontology = onto
    domain = [Model]
    range = [OperatingSystem]


class HaveProcessor(Property):
    ontology = onto
    domain = [Model]
    range = [Processor]


class HaveYearOfIntro(Property):
    ontology = onto
    domain = [Model]
    range = [YearOfIntro]


class HaveQuickCharge(Property):
    ontology = onto
    domain = [Model]
    range = [QuickCharge]


my_phone = Smartphone("my phone")
nokia = Brand("Nokia")
lumia6= Model("Lumia 600")
lumia7 = Model("Lumia 700")
gsm = GSMStandard("600/900")
weight = Weight("600 g")
battery = Battery("2000 mAh")

my_phone.HaveBrand.append(nokia)
nokia.HaveModel.append(lumia6)
nokia.HaveModel.append(lumia7)
lumia6.HaveGSMStandard.append(gsm)
lumia6.HaveWeight.append(weight)
lumia6.HaveBattery.append(battery)
lumia7.HaveGSMStandard.append(gsm)
lumia7.HaveWeight.append(weight)
lumia7.HaveBattery.append(battery)

print(my_phone.HaveBrand)
print(nokia.HaveModel)
print(lumia7.HaveBattery)


onto.save()
