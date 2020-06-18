![](.//media/CabeceraDocumentosMD.png)

# Hércules Backend ASIO. Método para el control de versiones OWL 

[INTRODUCCIÓN](#introducción)

[Procedimiento de desarrollo ontológico](#procedimiento-de-desarrollo-ontológico)

-   [Pasos del procedimiento de gestión de cambios en ROH](pasos-del-procedimiento-de-gestión-de-cambios-en-roh)

[Herramientas de control de versiones](#herramientas-de-control-de-versiones)

-   [Edición y versionado en WebProtégé](#edición-y-versionado-en-webprotégé)

-   [Publicación en GitHub](#publicación-en-github)

INTRODUCCIÓN
============

El presente documento describe el método para el control de versiones
OWL en el proyecto Hércules ASIO. Dicho método incluye el uso de dos
aplicaciones de control de versiones: WebProtégé
(<https://webprotege.stanford.edu/>) y Git (<https://github.com/>).

El proyecto Hércules ASIO dispone de una instancia de WebProtégé en:

http://herc-as-webprotege-desa.atica.um.es/

Contacte con el equipo de Hércules ASIO si desea acceso al repositorio.

Procedimiento de desarrollo ontológico
======================================

El equipo de diseño ontológico de GNOSS-Deusto ha trabajado en paralelo 
en diferentes aspectos de la ontología que luego han podido fusionarse 
sin problemas, con un control de cambios a nivel de documento de texto. 
Se ha utilizado la herramienta Protegé para edición de la ontología y git
con la plataforma GitHub para llevar a cabo la gestión de cambios. 

Durante el desarrollo del proyecto no se ha utilizado WebProtegé ya que 
hemos considerado que no es la herramienta de desarrollo más adecuada, ya 
que no dispone de todas las funcionalidades de su versión de escritorio. 
Al utilizar la herramienta de control de versiones git, y la plataforma 
GitHub, se pueden utilizar todas las herramientas de Integración Continua (CI) 
disponibles para cualquier proyecto software. De esta manera, se podría 
emplear la técnica de pull-request para que, cuando un colaborador externo 
desease modificar la ontología, el equipo mantenedor del proyecto pudiera 
revisar esos cambios y aceptarlos si proceden.

Sin embargo, el proceso de revisión de un cambio no tiene por qué ser 
totalmente manual. A través de la herramienta [Github Actions](https://github.com/features/actions) se pueden 
definir unos flujos de ejecución que, por ejemplo, realicen una serie de
tests para comprobar que a pesar de los cambios realizados en la ontología
el resto de las herramientas dependientes siguen funcionando correctamente. 
Una vez pasados estos tests (batería de tests de regresión), el pull-request
se puede integrar en la rama principal del repositorio de la ontología. 
Si se desease utilizar una solución independiente de la plataforma Github, 
se podría utilizar la popular herramienta de integración continua [Jenkins](https://www.jenkins.io/).

En definitiva, consideramos que WebProtégé es una herramienta que permite
discernir los cambios efectuados dentro de la ontología no como cambios 
en contenidos textuales, sino como operaciones sobre la ontología. Por 
ejemplo, “se ha modificado una entidad”, “se ha añadido una nueva object
property”, etc. Sin embargo, no permite la integración de razonadores y 
otras características importantes en el diseño ontológico. 

No obstante, la solución final que proponemos es combinar WebProtegé con 
GitHub y herramientas de integración continua para garantizar una gestión
de cambios de calidad dentro de ROH. Por ejemplo, utilizaríamos WebProtegé
para implementar el prototipo de un cambio importante dentro de la ontología,
pero este cambio, una vez consensuado, tendría que ser trasladado al
repositorio git para ser integrado dentro de la rama principal a través del
mecanismo pull-request.

Pasos del procedimiento de gestión de cambios en ROH
----------------------------------------------------

El procedimiento de gestión de cambios en la red de ontologías ROH tendrá 
los siguientes pasos:

1.	**Edición colaborativa en WebProtégé**. Hacer un Branch de la ontología en GitHub y trabajar de modo colaborativo con WebProtégé. El fichero que genera Protégé (la versión de escritorio) no deja los contenidos en el mismo orden cuando diferentes usuarios modifican concurrentemente el mismo, lo cual produce quebraderos de cabeza durante la integración (merge) de los mismos. Webprotegé, sin embargo, permite mantener el historial de cambios dentro de una ontología, independientemente de la serialización. 
2.	**Pull request para solicitar revisión y aceptación de cambios**. Cuando una revisión consolidada de la ontología desarrollada en modo colaborativo en WebProtégé es concluida, se realizará un PULL REQUEST para integrar cambios realizados con WebProtégé con la versión release en la rama principal de la ontología, mantenida en el repositorio GitHub.  
3.	**Aceptación de los cambios e integración en rama principal**. Si los cambios realizados no *rompen* el sistema ASIO (se valida que los tests de regresión que comprueban el buen funcionamiento de la ontología y de las herramientas que dependen de ella se ejecutan correctamente), entonces son aceptados como nueva versión de ROH. 

Todos los cambios a los que estaría sujetos la ontología serían supervisados
por el equipo mantenedor del proyecto, por lo que la aceptabilidad de los 
mismos dependerá de dicho equipo. Sin embargo, hay ciertos cambios, como 
modificaciones en propiedades como rdfs:label o rdfs:comment, que, en principio,
no deberían tener mayores repercusiones en el resto de componentes. Para otros
cambios, como la introducción o modificación de clases y propiedades o de las
relaciones entre ellas, se propone un enfoque híbrido a través de tests 
automatizados y la confirmación final del equipo mantenedor.

Herramientas de control de versiones
====================================

Como ya hemos comentado, proponemos el uso de WebProtégé para gestionar
el prototipado de los cambios importantes dentro de la ontología, mientras
que las versiones liberadas de la(s) ontología(s) se subirán a GitHub.

WebProtégé está disponible en la infraestructura de desarrollo de
Hércules ASIO en:

http://herc-as-webprotege-desa.atica.um.es/

Contacte con el equipo de Hércules ASIO si desea acceso al repositorio.

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
manera eficaz, mientras que en GitHub se generan ramas y se consolidan 
nuevas versiones de las ontologías. 

Además, GitHub permite la descarga de las versiones de las ontologías y 
mantiene un registro de las versiones consolidadas.

El repositorio de código fuente GitHub para el desarrollo de la 
infraestructura ontológica del proyecto Hércules está en
<https://github.com/HerculesCRUE/GnossDeustoOnto/>.

