from rdflib import Graph, Namespace
import owl


def generate_query(namespace, params):
    """
    :param namespace - przestrzen nazw
    :param params - lista zawierajaca dicty o kluczach (property, value, operator?, value?)
    gdzie property to specyfikacja telefonu (np. 'HaveBattery'),value to wartosc specyfikacji (np. 5000 [mAh]),
    operator jest opcjonalny, zawiera rodzaj filtru '<' lub '>', value (opcjonalny) wartość filtru
    """
    query = 'SELECT ?phone WHERE {'
    for param in params:
        query += ' ?phone <' + getattr(namespace, param['property']) + '> ' + param['value'] + '. '
    query += '}'
    return query

#  http://mowl-power.cs.man.ac.uk:8080/converter/convert
if __name__ == '__main__':
    g = Graph()
    g.parse('data/ontology.rdf')

    otk = Namespace("file:///home/akus/Projekty/zti/otk/data/newest_onto.owlnewest_onto.owl#")

    # for x in g:
    #     print(x)
    # select = ['file:///home/akus/Projekty/zti/otk/data/new_onto.owlnew_onto.owl#Lumia_600']
    # where = ['<{}> <{}> {} .'.format(select[0], 'file:///home/akus/Projekty/zti/otk/data/new_onto.owlnew_onto.owl#HaveBattery', '?battery')]
    # qres = g.query('SELECT ?batery WHERE {' + where[0] + '}')

    # qres = g.query('SELECT ?batery WHERE { <file:///home/akus/Projekty/zti/otk/data/new_onto.owlnew_onto.owl#Lumia_600> <file:///home/akus/Projekty/zti/otk/data/new_onto.owlnew_onto.owl#HaveBattery> ?batery }')

    qres = g.query('SELECT ?phone WHERE {'
                   ' ?phone <file:///home/akus/Projekty/zti/otk/data/new_onto.owlnew_onto.owl#HaveBattery> "5000"^^<http://www.w3.org/2001/XMLSchema#string>. '
                   ' ?phone <file:///home/akus/Projekty/zti/otk/data/new_onto.owlnew_onto.owl#HaveWeight> "1000"^^<http://www.w3.org/2001/XMLSchema#string>'
                   '}')
    for row in qres:
        print("ROW: {}".format(row))

