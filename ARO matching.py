from pronto import Ontology

cl = Ontology("http://purl.obolibrary.org/obo/cl.obo")
#for ARGs (ARO for antibiotic resistance ontology--aro.owl from https://card.mcmaster.ca/download)

aro = Ontology.from_obo_library("aro.owl")
#exploring ontology
cf = aro['confers_resistance_to_antibiotic']
t = aro['ARO:1000001']
list(t.objects(cf))
list(t.superclasses())
list(t.subclasses())

#change format to obo
with open('aro.obo', 'wb') as f:
    aro.dump(f, format = 'obo')
    
#find terms
aro = Ontology("aro.obo")
for term in aro.terms():
    if term.is_leaf():
        print(term.id)
        
#load resfinder sequences for matching
import pandas as pd
resfinder_seq = pd.read_csv("resfinder.csv", sep=" ", header=None)
aro2seq = {}
for a in set(resfinder_seq['#Aminoglycoside']):
    if a not in aro:
        continue
    t = aro[a]
    cf = aro['name.lower()']
    cur = list(t.subclasses(cf))
    if cur:
        aro2seq[a] = ';'.join([c.name for c in cur])
        
pd.DataFrame({'Matching_ARO': pd.Series(aro2seq)
             }).to_csv('aro2seq.csv', sep = '\t')
