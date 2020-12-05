from pronto import Ontology

cl = Ontology("http://purl.obolibrary.org/obo/cl.obo")
aro = Ontology.from_obo_library("aro.owl")
cf = aro['confers_resistance_to_antibiotic']
