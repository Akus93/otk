from rdflib import Graph


def generate_query(namespace, params):
    """
    :param namespace - przestrzen nazw
    :param params - lista zawierajaca dicty o kluczach (property, value, type)
    gdzie property to specyfikacja telefonu (np. 'HaveBattery'),value to wartosc specyfikacji (np. 5000 [mAh]),
    type to typ wartości (np. boolean = <http://www.w3.org/2001/XMLSchema#boolean>)
    Przykład: generate_query(namespace, [{'property': 'HaveOperatingSystem', 'value': 'Android_6.0_Marshmallow', 'type': string},
                                            {'property': 'HaveRAM', 'value': '2', 'type': integer}])
    """
    query = 'SELECT ?phone WHERE {'
    for param in params:
        query += ' ?phone <' + namespace + param['property'] + '> \'' + param['value'] + '\'^^' + param['type'] + '.'
    query += ' }'
    return query


def search_phones(params):
    graph = Graph()
    graph.parse('../data/otk.rdf')

    namespace = "file:///home/akus/Projekty/zti/otk/server/data/otk.owlotk.owl#"
    string = '<http://www.w3.org/2001/XMLSchema#string>'
    boolean = '<http://www.w3.org/2001/XMLSchema#boolean>'
    integer = '<http://www.w3.org/2001/XMLSchema#integer>'

    types = {
        'HaveGSMStandard': string,
        'HaveWeight': integer,
        'HaveBattery': integer,
        'HaveScreen': boolean,
        'HaveScreenProtection': boolean,
        'HaveMemory': integer,
        'HaveRAM': integer,
        'HaveOperatingSystem': string,
        'HaveProcessor': string,
        'HaveYearOfIntro': string,
        'HaveQuickCharge': string,
        'HaveTouchScreen': string,
        'HaveAccelerometer': string,
        'HaveProximitySensor': string,
        'HaveLightSensor': string,
        'Magnetometer': string,
        'HaveGyroscope': string,
        'HaveBarometer': string,
        'HaveAltimeter': string,
        'HaveGravitySensor': string,
        'HaveIrisScanner': string,
        'HaveFingerprintScanner': string,
        'HaveThermometer': string,
        'HaveHygrometer': string,
    }
    query_params = []
    for param in params:
        if params[param] is not None and params[param]:
            if params[param] is True:
                params[param] = 'True'
            query_params.append({'property': param, 'value': str(params[param]), 'type': types[param]})
    query = generate_query(namespace, query_params)
    print(query)
    query_result = graph.query(query)
    return query_result


if __name__ == '__main__':
    g = Graph()
    g.parse('../data/otk.rdf')

    for x in g:
        print(x)

    # qres = g.query("SELECT ?phone WHERE { ?phone <file:///home/akus/Projekty/zti/otk/data/otk.owlotk.owl#HaveOperatingSystem> 'Android_6.0_Marshmallow'^^<http://www.w3.org/2001/XMLSchema#string>. "
    #                "?phone <file:///home/akus/Projekty/zti/otk/data/otk.owlotk.owl#HaveRAM> '2'^^<http://www.w3.org/2001/XMLSchema#integer>."
    #                "}")
    qres = g.query("SELECT ?phone WHERE { ?phone <file:///home/akus/Projekty/zti/otk/data/otk.owlotk.owl#HaveQuickCharge> 'true'^^<http://www.w3.org/2001/XMLSchema#boolean>. }")
    for row in qres:
        print("ROW: {}".format(row))
    print(len(qres))
