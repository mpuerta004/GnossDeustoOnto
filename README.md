![](./Documentation/media/CabeceraDocumentosMD.png)

# ROH - Red de Ontologías Hércules

The University of Murcia signed on November 29, 2017, a Covenant with the Ministry of Economy, Industry and Competitiveness backing the “HÉRCULES: Semantic University Research Data” Project with a budget of FIVE MILLION FOUR HUNDRED AND SIXTY-TWO THOUSAND SIX HUNDRED euros with an 80% of co-financiering from the European Regional Development Fund program (ERDF) within the 2014-2020 period. 

The project arose as a CRUE initiative, to create the basis for a new collaboration model between universities, to develop the information management systems and with the main objective of encouraging this type of collaboration.

Therefore, the purpose of this agreement was to contribute to the improvement of public services and business innovation and research through the improvement of:
* efficiency in public investment by decreasing the duplication of investment in R&D.
* efficiency of research in universities.
* scientific dissemination of research results.
* detection of synergies in R&D between universities.
* transfer of R&D results to companies.
* efficiency in the management of research. 
* by creating a research management system with semantic capacities based on semantic open data and that will provide a global view of the research data contained in the Spanish University System.

ROH stands for Red de Ontologías Hércules (Hercules Ontology Network).

## Documentation
The ROH network of ontologies is divided into 3 main parts. 
* The generic ontology, named ROH, contains the most important entities and properties to model information in the academic domain. It contains the most important part of the network of ontologies. It covers the academic domain, being agnostic to the country or the research organization whose information wants to be modelled with it. 
* ROHES is a specialization of ROH for the Spanish science and research domain. It includes some additional entities which are only used in the Spanish science and research domain, e.g. rohes:Sexenio or rohes:ProfesorTitularDeEscuelaUniversitaria. 
* Finally, ROHUM is a specialization to cater with the special modelling needs of University of Murcia. More concretely, a wide range of entities to support the accounting system and be able to model expense types are included, e.g. rohum:ArrendamientosYCanones or rohum:InversionNueva.

The following subsections provide documentation about the Hercules Network of Ontologies (ROH). 
* Firstly, readers should explore the [ROH Tutorial & ROH reference specification](#headManualDoc)
* Secondly, readers can access to the automatically generated documentation, thanks to Widoco, where full details about the entities, object and data type properties for each of the entities modelled in the different parts of teh network of ontologies are described: [ROH](#headROH), [ROHES](#headROHES), [ROHUM](#headROHUM). 

A section to review the [FAIR principles](#headFAIR) compliance of ROH has also been included. 


The documentation is classified into manually generated and automatically generated documentation.  
### <a name="headManualDoc"></a>`ROH Tutorial & ROH reference specification`
- [ROH Tutorial](https://github.com/HerculesCRUE/GnossDeustoOnto/tree/master/Documentation). This manually generated documentation is written in Markdown format. It is recommended to be read firstly. This documentation illustrates with diagrams how each main entity in ROH relates to other entities. It also includes for each entity a table listing its subclasses, object and data properties, which should be used by whoever wants to populate with instance data ROH. 
- [ROH Reference specification](https://github.com/HerculesCRUE/GnossDeustoOnto/blob/master/Documentation/1-%20OntologyDocumentation.pdf). This document details in tabular form, for each ontology concept, each subclasses, object and datatype properties.

Next sections contain the automatically generated documentation with Widoco and the ROH validation results returned by the tool OOPs:

### <a name="headROH"></a>`roh`

- [Widoco](https://deustohercules.github.io/roh/roh/index.html)
- [OOPs](https://deustohercules.github.io/roh/roh/OOPSevaluation/oopsEval.html)

### <a name="headROHES"></a>`rohes`

- [Widoco](https://deustohercules.github.io/roh/rohes/index.html)
- [OOPs](https://deustohercules.github.io/roh/rohes/OOPSevaluation/oopsEval.html)


### <a name="headROHUM"></a>`rohum`

- [Widoco](https://deustohercules.github.io/roh/rohum/index.html)
- [OOPs](https://deustohercules.github.io/roh/rohum/OOPSevaluation/oopsEval.html)

### <a name="headFAIR"></a>`FAIR tests`
- [FAIR test for ROH ontology](https://fairsharing.github.io/FAIR-Evaluator-FrontEnd/#!/evaluations/4046)
