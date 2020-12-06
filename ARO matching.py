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
resfinder_seq = pd.read_csv("beta-lactam.csv", sep=" ", header=None)
* if permission denied, change access 
$ chmod 755 beta-lactam.csv

#now match aro info to resfinder_seq
