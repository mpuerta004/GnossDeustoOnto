import argparse
from rdflib import Graph
from rdflib.namespace import RDF, SKOS
from rdflib.term import URIRef

parser = argparse.ArgumentParser()
parser.add_argument("source", help="URL or directory of source SKOS concepts")
parser.add_argument("output", help="output file for generated triples")
args = parser.parse_args()

source_graph = Graph()
source_graph.parse(args.source)

for s, p, o in source_graph.triples((None, RDF.type, SKOS.Concept)):
    source_graph.add((s, RDF.type, URIRef(u"http://purl.org/roh#UNESCOKnowledgeArea")))

s = source_graph.serialize(args.output, format='xml')