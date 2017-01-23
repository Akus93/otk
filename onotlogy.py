from owlready import *
from SPARQLWrapper import SPARQLWrapper, JSON

onto = Ontology("oldonto.owl")
onto_path.append("/home/akus/Projekty/zti/otk/data")


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


my_phone = Smartphone("my_phone")
my_phone1 = Smartphone("my_phone1")
first_brand = Brand("Samsung")
second_brand = Brand("Nokia")
first_model = Model("Lumia")
second_model = Model("S6")

my_phone.HasBrandName.append(first_brand)
first_brand.HasModel.append(second_model)
my_phone1.HasBrandName.append(second_brand)
second_brand.HasModel.append(second_model)


print(onto.properties)
onto.save()
print(to_owl(onto))

# sparql = SPARQLWrapper("http://dbpedia.org/sparql")
# sparql.setQuery("""
#     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#     SELECT ?label
#     WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label }
# """)
# sparql.setReturnFormat(JSON)
# results = sparql.query().convert()
#
# for result in results["results"]["bindings"]:
#     print(result["label"]["value"])
