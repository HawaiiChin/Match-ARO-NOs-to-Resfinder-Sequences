import pronto
from glob import glob
aro = pronto.Ontology('aro.owl')

name2id = {}
for t in aro.terms():
    name2id[t.name] = t.id
    for syn in t.synonyms:
        assert syn.scope == 'EXACT'
        name2id[syn.description] = t.id

name2id = {k.lower():v for k,v in name2id.items()}

matched = []
unmatched = []
for fname in glob('notes.txt'):
    for line in open(fname):
            gene = line.split(':')[0]
            if gene.lower() in name2id:
                matched.append(gene)
            elif gene[:3] == 'bla':
                gene = gene[4:]
                if gene.lower() in name2id:
                    matched.append(gene)                
            else:
                unmatched.append(gene)

frac = (len(matched)/(len(unmatched)  + len(matched)))
print(f'Matched {len(matched)} of {len(matched)+len(unmatched)} ({frac:.2%}) of identifiers')

pd.DataFrame({'Matching_ARO': pd.Series(matched)
             }).to_csv('aro2seq.csv', sep = '\t')
pd.DataFrame({'Matching_ARO': pd.Series(unmatched)
             }).to_csv('!aro2seq.csv', sep = '\t')
