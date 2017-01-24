from owlready import *
import os

path = '/'.join(os.path.realpath(__file__).split('/')[:-1]) + '/data'
onto = Ontology("otk.owl")
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
    range = [str]


class HaveTouchScreen(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveAccelerometer(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveProximitySensor(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveLightSensor(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveMagnetometer(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveGyroscope(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveBarometer(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveAltimeter(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveGravitySensor(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveIrisScanner(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveFingerprintReader(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveThermometer(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]


class HaveHygrometer(FunctionalProperty):
    ontology = onto
    domain = [Model]
    range = [str]

