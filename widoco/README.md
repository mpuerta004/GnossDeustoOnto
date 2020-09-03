# Documentation generation with WIDOCO

## Generating the docs

```
./generate.sh
```

## Changing the reference section

1. Edit the `WIDOCO_REFERENCES_CONTENT` variable in `widoco-compile-config`, for example:
    ```
    WIDOCO_REFERENCES_CONTENT='This ontology has the following classes and properties. A more in-depth explanation of the main entities in ROH and the relationship among them is given in ROH Tutorial. You should read this document to understand how academic knowledge is modelled in ROH  (<a href="https://github.com/HerculesCRUE/GnossDeustoOnto/tree/master/Documentation">https://github.com/HerculesCRUE/GnossDeustoOnto/tree/master/Documentation</a>). ROH Reference Specification (<a href="https://github.com/HerculesCRUE/GnossDeustoOnto/blob/master/Documentation/1-%20OntologyDocumentation.pdf">https://github.com/HerculesCRUE/GnossDeustoOnto/blob/master/Documentation/1-%20OntologyDocumentation.pdf</a>) offers an overview in tabular form for each of the entities, giving details on the object and data properties supported by each entity in ROH. This document is very useful when instances of ROH want to be created, since it clearly explains what entity types a given entity type relates with through an object property and what data properties are supported by a given entity type, including details about its associated object types.'
    ```

Please be careful, the value should be contained in one single line.

2. Recompile WIDOCO:
    ```
    ./widoco-compile.sh
    ```

3. Commit the new version of `widoco-custom.jar`
    