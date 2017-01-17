from owlready import *

onto = Ontology("new_onto.owl")
onto_path.append("/home/ania/PycharmProjects/otk/otk_pl/otk_pl")


class Smartphone(Thing):
    ontology = onto


class Brand(Thing):
    ontology = onto


class Model(Thing):
    ontology = onto


# class GSMStandard(Thing):
#     ontology = onto
#
#
# class Weight(Thing):
#     ontology = onto
#
#
# class Battery(Thing):
#     ontology = onto
#
#
# class Screen(Thing):
#     ontology = onto
#
#
# class ScreenProtection(Thing):
#     ontology = onto
#
#
# class Memory(Thing):
#     ontology = onto
#
#
# class RAM(Thing):
#     ontology = onto
#
#
# class OperatingSystem(Thing):
#     ontology = onto
#
#
# class Processor(Thing):
#     ontology = onto
#
#
# class YearOfIntro(Thing):
#     ontology = onto
#
#
# class QuickCharge(Thing):
#     ontology = onto


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
    range = [str]


class HaveBattery(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


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
    range = [str]


class HaveRAM(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


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
    range = [str]


my_phone = Smartphone("my phone")
nokia = Brand("Nokia")
lumia6= Model("Lumia 600")
lumia7 = Model("Lumia 700")
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
lumia6.HaveWeight = "600 g"
lumia6.HaveBattery = "2000 mAh"
lumia7.HaveGSMStandard = "600/900"
lumia7.HaveWeight = "600 g"
lumia7.HaveBattery = "2000 mAh"

print(my_phone.HaveBrand)
print(nokia.HaveModel)
print(lumia7.HaveBattery)
print(my_phone)




onto.save()
