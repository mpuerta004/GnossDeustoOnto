# Instalación

Requisitos:

- Python 3
- Pipenv

Instalamos con Pipenv:

```bash
$ pipenv install
```

A continuación, accedemos a la shell:

```bash
$ pipenv shell
```

# Ejecución

## Generar un archivo turtle a partir de un xml

```bash
$ python3 main.py entrada salida orcid
```

- `entrada`: el archivo XML que queremos convertir
- `salida`: ubicación (incluyendo el nombre) donde queremos que se cree el archivo 

Ejemplo:

```bash
$ python3 main.py examples/cvn_202033-Diego.xml diego.xml 0000-0001-8055-6823 --format pretty-xml
```

Posibles formatos: (argumento `--format`)

- `xml`
- `n3`
- `turtle` (por defecto)
- `nt`
- `pretty-xml`
- `trix`
- `trig`
- `nquads`

Para obtener ayuda:

```
$ python3 main.py --help
```
