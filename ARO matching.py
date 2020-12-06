from pronto import Ontology

cl = Ontology("http://purl.obolibrary.org/obo/cl.obo")
```#for ARGs here (ARO for antibiotic resistance ontology--aro.owl from https://card.mcmaster.ca/download)

aro = Ontology.from_obo_library("aro.owl")

```#exploring ontology
cf = aro['confers_resistance_to_antibiotic']
t = aro['ARO:XXXXXXX']
list(t.objects(cf))
list(t.superclasses())
list(t.subclasses())

```#load resfinder sequences for matching
import pandas as pd
resfinder_seq = pd.read_txt("sequence.txt", sep=" ", header=None)
