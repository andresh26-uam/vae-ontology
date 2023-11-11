import types
from typing import List
from nltk.corpus import wordnet

from owlready2  import Property, Ontology, get_ontology, ObjectPropertyClass, ThingClass,ClassAtom

import nltk
from rdflib import URIRef 
#nltk.download('wordnet')

onto: Ontology = get_ontology("file://vaeontology.rdf").load()

# Search for synonyms and antonyms using WordNet
classes: List[ThingClass] = [c for c in onto.classes()]

values_classes = onto.search(iri = '*SchwartzValues#[A-Z]*')
value_concept_class = onto.search(iri = '*ValueConcept')[0]

synonyms = set()
antonyms = set()

for valuec in values_classes:
    word = valuec.name.lower()
    for syn in wordnet.synsets(word):
        # Selecting relevant synsets.
        if word == "value":
            # This is just the class bhv:Value.
            continue
        if word == "power":
            if '05' not in syn.name():
                # one possessing or exercising power or influence or authority (synset 5)
                continue
        if word == "security":
            if '01' not in syn.name() or '03' not in syn.name():
                continue
        if word == "focus":
            if '01' not in syn.name() or '03' not in syn.name() :
                continue
        if word == "stimulation":
            if '01' not in syn.name() or 'foreplay' in syn.name():
                continue
        if word == "benevolence":
            if '01' not in syn.name():
                continue
        if word == "dominance":
            if '02' not in syn.name() or '01' not in syn.name():
                continue
        if word == "conservation":
            if '01' not in syn.name() or '02' not in syn.name():
                continue
        if word == "concern":
            if 'concern.n.01' not in syn.name() or '02' not in syn.name() or '03' not in syn.name() or '04' not in syn.name():
                continue    
        if word == "nature":
            if '04' not in syn.name() or '03' not in syn.name():
                continue
        if word == "caring":
            if 'care.v.01' not in syn.name() or 'caring.s.01' not in syn.name() or 'worry.v.02'  not in syn.name():
                continue    
        if word == "thought":
            if 'thinking.n.01' not in syn.name() or 'think.v.08' not in syn.name() or 'think.v.03'  not in syn.name() or 'think.v.13' not in syn.name():
                continue 
        if word == "action":
            if 'action.n.06' not in syn.name() or 'action.n.02' not in syn.name():
                continue 
        if word == "face":
            if 'face.n.03' not in syn.name() or 'face.n.11' not in syn.name() or 'boldness.n.02' not in syn.name():
                continue 
        

        for lemma in syn.lemmas():
            if lemma.name().lower() != word:
                synonyms.add(lemma.name())

                if len(onto.search(iri='*' + lemma.name().capitalize() + '*')) == 0:
                    with onto:
                        cls = types.new_class(lemma.name().capitalize(), (valuec,))
                        print(cls)
                        print(cls.is_a)
                        cls.label = [lemma.name().capitalize(),]
                        cls.comment = [f"{lemma.name().capitalize()}: {syn.definition()}", "Term added automatically"]
                        cls.namespace = onto.get_namespace('https://w3id.org/def/vaeontology#')
                        

print(synonyms)

onto.save("vaeontology_nor.rdf",)