![](.//media/CabeceraDocumentosMD.png)

# Hércules Backend ASIO. Método para el control de versiones OWL 

[1 INTRODUCCIÓN](#introducción)

[2 Procedimiento](#procedimiento)

[2.1 Edición y versionado en WebProtégé](#edición-y-versionado-en-webprotégé)

[2.2 Publicación en GitHub](#publicación-en-github)

INTRODUCCIÓN
============

El presente documento describe el método para el control de versiones
OWL en el proyecto Hércules. Dicho método incluye el uso de dos
aplicaciones de control de versiones: WebProtégé
(<https://webprotege.stanford.edu/>) y Git (<https://github.com/>).

Procedimiento
=============

El trabajo continuo se gestiona mediante WebProtégé, mientras que las
versiones liberadas de la(s) ontología(s) se subirán a GitHub.

WebProtégé estará disponible en la infraestructura de desarrollo de
Hércules ASIO.

Edición y versionado en WebProtégé
----------------------------------

Los desarrolladores pueden crear y editar ontologías de dos maneras
distintas:

-   Online: A través del editor de ontologías de WebProtégé. Los
    desarrolladores pueden hacer los cambios que necesiten desde el
    editor online de WebProtégé y automáticamente se guarda y versiona
    la ontología.

> ![](.//media/image2.png)

-   Offline: A través del entorno que deseen (Protégé, FluentEditor,
    OWLGrEd...). El desarrollador debe descargarse desde WebProtégé la
    última versión de la ontología y abrirla desde su editor de
    ontologías preferido. Para ello, vamos a la pestaña History y
    pinchamos en la versión que nos queremos descargar (en este caso, la
    R7 que es la última). Nos aparece un menú, donde debemos seleccionar
    la opción "Download":

![](.//media/image3.png)

> Inmediatamente se descarga la ontología en formato OWL.
>
> Una vez ha terminado la edición, debe subir la ontología en la que ha
> trabajado a WebProtégé. La ontología puede subirse en múltiples
> formatos (owl, ttl, rdfs...). Para ello, nos dirigimos al menú
> "Project" y pinchamos en la opción Apply External Edits:
>
> ![](.//media/image4.png)
>
> Seleccionamos el archivo que hemos editado y aceptamos. Antes de
> guardar la nueva versión de la ontología, WebProtégé muestra un
> diálogo con los cambios detectados respecto a la versión almacenada.
>
> ![](.//media/image5.png)

Podemos añadir un mensaje para dejar reflejado en el histórico de
versiones el motivo de la modificación.

Publicación en GitHub
---------------------

WebProtégé sirve para versionar el trabajo diario de los desarrolladores
y resolver los posibles conflictos de edición que puedan aparecer de
manera eficaz. Cada vez que se desee consolidar una versión de la
ontología, debe descargarse desde WebProtégé el archivo OWL de la
ontología y subirlo al repositorio de código fuente GitHub del proyecto
Hércules <https://github.com/HerculesCRUE/GnossDeustoBackend>, dentro de
la carpeta Ontologies. Si se considera necesario, se podrá crear una
carpeta para cada ontología.
