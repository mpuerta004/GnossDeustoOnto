#
# main.py
# Parte de HERCULES-ASIO
# ----------------------
# Genera, a partir de un archivo XML CVN, tripletas RDF compatibles con ROH.
#
# ** EN DESARROLLO **
#
import argparse
import xml.etree.ElementTree as ET
from rdflib import Graph, Namespace, Literal, URIRef, BNode
from rdflib.namespace import RDF, FOAF, NamespaceManager
import secrets  # temporal, para generar las ID de ciertas entidades
import urllib.parse

# Caché para los nombres de códigos
code_name = {}

def main():
    tree = ET.parse(args.filename)
    root = tree.getroot()

    # Crear el grafo, lo iremos rellenando más abajo
    # Le inyectamos el término corto de la ontología roh

    namespace_manager = NamespaceManager(Graph())
    roh = Namespace("https://purl.org/roh/")
    namespace_manager.bind('roh', roh, override=False)
    bibo = Namespace("http://purl.org/ontology/bibo/")
    namespace_manager.bind('bibo', bibo, override=False)
    vivo = Namespace("http://vivoweb.org/ontology/core#")
    namespace_manager.bind('vivo', vivo, override=False)
    g = Graph()
    g.namespace_manager = namespace_manager

    person = URIRef("https://purl.org/roh/researcher/"+ str(args.orcid))

    # Vamos a ir recorriendo el árbol XML del documento CVN e iremos sacando, cuando sea necesario, información, para
    # luego insertarla en tripletas generadas al vuelo con rdflib
    for child in root:
        code = node_get_code(child)

        if args.verbose:  # Debug
            print("> " + code + ": " + code_get_name(code, args.lang))

        # TODO hacer switch

        # Identificación CVN
        if code == "000.010.000.000":
            first_name, first_family_name, second_family_name, email = None, None, None, None
            for subchild in child:
                subcode = node_get_code(subchild)

                if args.verbose:  # Debug
                    print(">> " + subcode + ": " + code_get_name(subcode))

                # TODO hacer switch

                # Apellidos
                if node_get_code(subchild) == "000.010.000.010":
                    first_family_name = subchild.find("{http://codes.cvn.fecyt.es/beans}FirstFamilyName").text
                    second_family_name = subchild.find("{http://codes.cvn.fecyt.es/beans}SecondFamilyName").text

                # Nombre
                if node_get_code(subchild) == "000.010.000.020":
                    first_name = subchild.find("{http://codes.cvn.fecyt.es/beans}Value").text

                # Email
                if node_get_code(subchild) == "000.010.000.230":
                    email = subchild.find("{http://codes.cvn.fecyt.es/beans}Value").text

            # Person
            g.add((person, RDF.type, roh.Researcher))
            # Person > name
            full_name = first_name + " " + first_family_name + " " + second_family_name
            g.add((person, FOAF.name, Literal(full_name)))
            # Person > email
            g.add((person, FOAF.mbox, Literal(email)))

        # Publicaciones, documentos científicos y técnicos (ResearchObject)
        if code == "060.010.010.000":
            title, journal, volume, page_start, page_end, doi, issn = None, None, None, None, None, None, None # TODO sustituir por diccionarios

            for subchild in child:
                subcode = node_get_code(subchild)

                if args.verbose:  # Debug
                    print(">> " + subcode + ": " + code_get_name(subcode))

                # TODO hacer switch

                # Título
                if node_get_code(subchild) == "060.010.010.030":
                    title = subchild.find("{http://codes.cvn.fecyt.es/beans}Value").text
                    if args.verbose:  # Debug
                        print(">>> TÍTULO: " + str(title))

                # Journal
                if node_get_code(subchild) == "060.010.010.210":
                    try:
                        journal = subchild.find("{http://codes.cvn.fecyt.es/beans}Value").text
                    except AttributeError as e: 
                        if args.verbose:  # Debug
                            print(">>> JOURNAL: error")
                    if args.verbose:  # Debug
                        print(">>> JOURNAL: " + str(journal))

                # Volume
                if node_get_code(subchild) == "060.010.010.080":
                    try:
                        volume = subchild.find("{http://codes.cvn.fecyt.es/beans}Volume").text
                    except AttributeError as e: 
                        if args.verbose:  # Debug
                            print(">>> VOLUMEN: error")
                    if args.verbose:  # Debug
                        print(">>> VOLUMEN: " + str(volume))

                # Páginas inicio y fin
                if node_get_code(subchild) == "060.010.010.090":
                    try:
                        page_start = subchild.find("{http://codes.cvn.fecyt.es/beans}InitialPage").text
                        page_end = subchild.find("{http://codes.cvn.fecyt.es/beans}FinalPage").text
                    except AttributeError as e: 
                        if args.verbose:  # Debug
                            print(">>> PÁGINAS: error")
                    
                    if args.verbose:  # Debug
                        print(">>> PÁGINAS: " + str(page_start) + "-" + str(page_end))

                # ISSN Journal
                if node_get_code(subchild) == "060.010.010.160":
                    try:
                        issn = subchild.find("{http://codes.cvn.fecyt.es/beans}Value").text
                    except AttributeError as e: 
                        if args.verbose:  # Debug
                            print(">>> ISSN JOURNAL: error")
                    if args.verbose:  # Debug
                        print(">>> ISSN JOURNAL: " + str(issn))

                # DOI
                if node_get_code(subchild) == "060.010.010.400":
                    try:
                        if subchild.find("{http://codes.cvn.fecyt.es/beans}Type").text == "040": # SOLO DOI, número mágico :S
                            doi = subchild.find("{http://codes.cvn.fecyt.es/beans}Value").text
                    except AttributeError as e:
                        if args.verbose:  # Debug
                            print(">>> DOI: error")
                    if args.verbose:  # Debug
                        print(">>> DOI: " + str(doi))

            if doi is None:
                publication = URIRef("https://purl.org/roh/article/" + str(secrets.token_hex(6)))  # TODO integrar backend generador URIs desarrollado por GNOSS
            else:
                publication = URIRef("https://purl.org/roh/article/" + urllib.parse.quote_plus(str(doi)))
            g.add((publication, RDF.type, bibo.AcademicArticle))
            g.add((publication, roh.title, Literal(str(title))))
            # Journal object
            if journal is not None:
                # Generar a URI
                if issn is None:  # Si no hemos detectado el ISSN, generamos un número al azar
                    journal_object = URIRef("https://purl.org/roh/journal/" + urllib.parse.quote_plus(str(secrets.token_hex(6))))
                else:
                    journal_object = URIRef("https://purl.org/roh/journal/" + urllib.parse.quote_plus(str(issn)))
                g.add((journal_object, RDF.type, bibo.Journal))
                g.add((journal_object, roh.title, Literal(str(journal))))
                g.add((journal_object, vivo.publicationVenueFor, publication))
                if issn is not None:
                    g.add((journal_object, bibo.issn, Literal(str(issn))))
            if volume is not None:
                g.add((publication, bibo.volume, Literal(str(volume))))
            if (page_start is not None) and (page_end is not None):
                g.add((publication, bibo.start, Literal(str(page_start))))
                g.add((publication, bibo.end, Literal(str(page_end))))
            if doi is not None:
                g.add((publication, bibo.doi, Literal(str(doi))))
            # roh:correspondingAuthor
            g.add((publication, roh.correspondingAuthor, person))

            # Crear rol TODO personalizar el nombre del rol según el tipo
            # role_uri = URIRef("http://purl.obolibrary.org/obo/BFO_0000023")
            # TODO roles — lo tengo que consultar con Mikel y Diego


    # Serializar y guardar en un archivo con el formato que queramos
    g.serialize(format=args.format, destination=args.out)
    print("Generated output file in " + args.out)


def node_get_code(node):
    """
    Obtener el código CVN de un nodo XML.
    """

    if node.tag == "{http://codes.cvn.fecyt.es/beans}Code":
        return node.text

    find_result = node.find('{http://codes.cvn.fecyt.es/beans}Code')

    if find_result is None:
        for child in node:
            if child.tag == "{http://codes.cvn.fecyt.es/beans}Code":
                return child.text

    return find_result.text


def code_get_name(code, lang='spa'):
    """
    Obtener el nombre de un código CVN a partir de los mapeos XML.
    """
    if code in code_name:
        return code_name[code]
    tree = ET.parse('mappings/cvn/1.4.2_sp1/XSD/SpecificationManual.xml')  # hardcoded for now
    result = tree.getroot().find("./*Item[@code='" + code + "']/Name/NameDetail[@lang='" + lang + "']/Name").text
    code_name[code] = result
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convertir un archivo XML CVN a tripletas ROH")
    parser.add_argument('filename', help="El fichero XML a convertir")
    parser.add_argument('out', help="Nombre del fichero donde guardar el resultado")
    parser.add_argument('orcid', help="ID de ORCID de la persona del CVN")
    parser.add_argument('--verbose', action="store_true", help="DEBUG: muestra más mensajes al generar archivos (tiempo de generación elevado)")
    parser.add_argument('--lang', nargs='?', default='spa', help="DEBUG: idioma para los encabezados")
    parser.add_argument('--format', nargs='?', default='turtle', help="Formato de salida", choices=["xml", "n3", "turtle", "nt", "pretty-xml", "trix", "trig", "nquads"])
    global args
    args = parser.parse_args()

    main()

# 19/03/2020 Iñigo — lo que he podido en este poco tiempo, lo siento por el código desastroso :^(
